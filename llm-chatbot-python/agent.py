from llm import llm
from graph import graph
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import Tool
from llm import llm
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate

from tools.vector import kg_qa
from tools.cypher import cypher_qa

# You are a movie expert providing information about movies.
# Do not answer any questions using your pre-trained knowledge, only use the information provided in the context.
# agent_prompt = hub.pull('hwchase17/react-chat')
agent_prompt = PromptTemplate.from_template("""

You are a knowledge graph information retrieval, similarity measure, and recommendation expert about GIS program
Be as helpful as possible and return as much information as possible.
When some words (close, similar, recommendation/recommend) are mentioned in the question, use 'Vector Search Index', calculate semantic similarity of each 'ResearchInterest' node with the extracted input, and return at least 10 similar 'ResearchInterest' nodes 
Do not find information outside of this Neo4j database 
Do not answer any questions that do not relate to our knowledge graph.
Only the information provided in the knowledge graph or you can use research interest property to do recommendation based on the embeddings
When the question contains Professor(s), it is always "People" node instead of Professor node
When it comes to relationship between People and ResearchInterest, the relationship in the Cypher statement generation should be "hasResearchInterestOf"
When using "Vector Index Search" to find closely aligned or similar research interests according to the input, return at least top 20 "ResearchInterest" nodes
For "ResearchInterest" node, please only return the 'research_interest' attribute
For "People" node, it has attributes like 'NAME_CN', 'NAME_EN', 'Research Interests', 'URL'. Return these attributes according to the question 
For "City" node, it has attributes including "NAME_CN", "NAME_EN", "WKT"(geographical locations), "CityID"
For "Continent" node, it has attributes including "NAME_CN", "NAME_EN"
For "Country" node, it has attributes including "NAME_CN", "NAME_EN"
For "Department" node, it has attributes including "NAME_CN", "NAME_EN"
For "University" node, it has attributes including "NAME_EN", 
"Description_CN" (the description of the university in Chinese), 
"Description_EN" (the description of the university in English), "URL" (the official website of the university), and "ABBR" (the abbreviation of the university name)

When using "Graph Cypher QA Chain" involving 'research_interest' attribute, please make sure that the research interest from input is contained in the database, 
Ttherwise, please turn to use "Vector Index Search" tool to find out similar research interests first. then use 'Graph Cypher QA chain' tool  

For relationships, there are "hasResearchInterestOf", "isIn", "WorksAt", and "isSimilarTo". 
For "hasResearchInterestOf", it has the type of  ("People" node)-["hasResearchInterestOf"]->("ResearchInterest" node)
For "isIn" relationship, it can be the following types
(1) ("City" node)-["isIn"]->("Country" node) 
(2) ("Country" node)-["isIn"]->("Continent" node);
(3) ("Department" node)-["isIn"]->("University" node)
For "WorksAt" relationship, it can be ("People" node)-["WorksAt"]->("University" node)
For "isSimilarTo" relationship, you can get the similarity score between two professors in descending order. Should be undirected relationship. The example cypher statement can be: 
match (p1:People)-[r:isSimilarTo]-(p2:People)
where p1.NAME_EN = 'LIU, Xingjian'
return p2.NAME_EN, r.score
order by r.score DESC

When asking question referring to research interests, professors, and other additional information (university, city, etc), 
first please use Vector Search Index tool to find similar research interests,
then use Graph Cypher QA Chain tool with the input of these returned research interests and return the information from the question 
""
TOOLS:
------

You have access to the following tools:

{tools}

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

Begin!

Previous conversation history:
{chat_history}

New input: {input}
{agent_scratchpad}
""")


'''
llm: this is set to the instance of ChatOpenAI
tools:
    - Tools are objects that can be used by the Agent to perform actions
    - You will create multiple tools that can be used by the Agent to perform specific tasks.
    However, a tool is required for "general chat" so the agent can respond to a user's input when no other tool

# '''

tools = [
    Tool.from_function(
        name = "General Chat",
        description = "For general chat not covered by other tools",
        func = llm.invoke,
        return_direct = True
    ),
    Tool.from_function(
        name = "Vector Search Index",
        description="Provides information about research interest using Vector Search",
        func=kg_qa,
        return_direct=False
    ),
    Tool.from_function(
        name = "Graph Cypher QA Chain",
        description = "Provides information about GIS programs including Professor, ResearchInterest, University, Department, City, Country, and Continent",
        func = cypher_qa,
        return_direct=False
    )
]

memory = ConversationBufferWindowMemory(
    memory_key = 'chat_history',
    k = 5,
    return_messages = True
)

agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(
    agent = agent,
    tools = tools,
    memory = memory,
    verbose = True
)

def generate_response(prompt):
    """
    Create a handler that calls the Conversational agent and returns a response to be rendered in the UI
    :param prompt:
    :return:
    """
    response = agent_executor.invoke({"input": prompt})

    return response['output']

# Create a movie chat chain

# Create a set of tools

# Create chat history callback

# Create the agent

# Create a handler to call the agent