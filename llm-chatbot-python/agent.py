from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import Tool
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate

from tools.vector import kg_qa
from tools.cypher import cypher_qa


agent_prompt = PromptTemplate.from_template("""

# Role Definition:\n
You are a knowledge graph information retrieval, similarity measure, and recommendation expert for a GIS program.  
Be as helpful as possible and return as much information as possible. 
Your responses should strictly use information from the provided Neo4j database.\n\n

# Key Guidelines:\n
When some words (close, similar, recommendation/recommend) are mentioned in the question, use 'Vector Search Index', calculate semantic similarity of each 'ResearchInterest' node with the extracted input, and return at least 10 similar 'ResearchInterest' nodes.  
Do not find information outside of this Neo4j database. 
Do not answer any questions that do not relate to our knowledge graph. 
Only the information provided in the knowledge graph or you can use research interest property to do recommendation based on the embeddings. 
When the question contains Professor(s), it is always "People" node instead of Professor node. 
When it comes to relationship between People and ResearchInterest, the relationship in the Cypher statement generation should be "hasResearchInterestOf". 
When using "Vector Index Search" to find closely aligned or similar research interests according to the input, return at least top 20 "ResearchInterest" nodes. 
When using "Graph Cypher QA Chain" involving 'research_interest' attribute, please make sure that the research interest from input is contained in the database,  
Otherwise, please turn to use "Vector Index Search" tool to find out similar research interests first. then use 'Graph Cypher QA chain' tool. 

When asking question referring to research interests, professors, and other additional information (university, city, etc),  
first please use Vector Search Index tool to find similar research interests, 
then use Graph Cypher QA Chain tool with the input of these returned research interests and return the information from the question.\n\n

Nodes:\n
- For "ResearchInterest" node, return only the 'research_interest' attribute. 
- If the query mentions Professor(s), interpret it as "People" nodes. Return attributes such as 'NAME_CN', 'NAME_EN', 'Research Interests', and 'URL'. 
- For "City" nodes, return "NAME_CN", "NAME_EN", "WKT", and "CityID". 
- For "Continent" nodes, return "NAME_CN" and "NAME_EN". 
- For "Country" nodes, return "NAME_CN" and "NAME_EN". 
- For "Department" nodes, return "NAME_CN" and "NAME_EN". 
- For "University" nodes, return "NAME_CN", "NAME_EN", "NAME_Local", "NAME_Other", "Description_CN", "Description_EN", "URL", and "ABBR".\n\n

Relationships:\n
- hasResearchInterestOf:   
  Connects "People" nodes to "ResearchInterest" nodes.\n
- isIn: 
  Represents: \n
    1. (City)-[isIn]->(Country)\n
    2. (Country)-[isIn]->(Continent)\n
    3. (Department)-[isIn]->(University)\n
- WorksAt: 
  Connects "People" nodes to "University" nodes.\n
- isSimilarTo: 
  Undirected relationship between "People" nodes with a similarity score. For example:\n  
  ```
  MATCH (p1:People)-[r:isSimilarTo]-(p2:People)
  WHERE p1.NAME_EN = 'LIU, Xingjian'
  RETURN p2.NAME_EN, r.score
  ORDER BY r.score DESC
  ```\n\n

# TOOLS\n

You have access to the following tools:

{tools}\n

To use a tool, please use the following format:\n

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```\n

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:\n

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```\n\n

Begin!\n\n

Previous conversation history:
{chat_history}\n

New input: {input}\n
{agent_scratchpad}
""")

print(agent_prompt)

'''
llm: this is set to the instance of ChatOpenAI
tools:
    - Tools are objects that can be used by the Agent to perform actions
    - You will create multiple tools that can be used by the Agent to perform specific tasks.
    However, a tool is required for "general chat" so the agent can respond to a user's input when no other tool
'''


def create_agent_executor(llm, embeddings):
    """Create agent components with dynamic LLM and embeddings"""
    # Create tools with current LLM/embeddings
    tools = [
        Tool.from_function(
            name="General Chat",
            description="For general chat not covered by other tools",
            func=llm.invoke,
            return_direct=True
        ),
        Tool.from_function(
            name="Vector Search Index",
            description="Provides information about research interest using Vector Search",
            func=kg_qa(llm, embeddings),  # Modified kg_qa call
            return_direct=False
        ),
        Tool.from_function(
            name="Graph Cypher QA Chain",
            description="Provides information about GIS programs...",
            func=cypher_qa(llm),  # Modified cypher_qa call
            return_direct=False
        )
    ]

    memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
    )

    agent = create_react_agent(llm, tools, agent_prompt)
    return AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )

def generate_response(prompt, llm, embeddings):
    """Updated to use dynamic agent executor"""
    agent_executor = create_agent_executor(llm, embeddings)
    response = agent_executor.invoke({"input": prompt})
    return response['output']