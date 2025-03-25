import sys
import streamlit as st
from utils import write_message
from agent import generate_response


# Page Config
st.set_page_config("GISphere Ebert", page_icon="../GISphere.png",
                   layout="wide", initial_sidebar_state="expanded")

# Sidebar for API Key Input
with st.sidebar:
    st.header("Configuration")
    use_dev_key = st.checkbox("Use OpenAI o3-mini model sponsored by GISphere (limited usage)")

    if use_dev_key:
        openai_api_key = st.secrets.get("OPENAI_API_KEY", "")
        openai_base_url = st.secrets.get("OPENAI_BASE_URL", "")
    else:
        openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")
        openai_base_url = st.text_input("Enter OpenAI Base URL (optional):")

    # Model Selection
    openai_model_options = ["o3-mini (Recommanded)", "gpt-4o-mini", "gpt-4o"]
    openai_model = st.selectbox("Select a model:", openai_model_options, index=0)
    openai_model = openai_model.split(" ")[0]


# Greeting Message
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm the GISphere Chatbot! 🌍\n"
         "Using [GISphere Database](https://gisphere.info), I can help you find GIS programs and professors based on research interests.\n\n"
         "📜 Journal Article: GISphere Knowledge Graph for Geography Education: Recommending Graduate Geographic Information System/Science Programs [DOI](https://doi.org/10.1111/tgis.13283)\n\n"
         "🔗 GitHub Repository: [GISphereKG Chatbot](https://github.com/GIS-Info/GISphereKG-ChatBot)\n\n"
         "⚠️ *Note: This chatbot is powered by an LLM and may generate incorrect responses.*"}
    ]

# Submit handler
def handle_submit(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    # Handle the response
    with st.spinner('Thinking...'):
        response = generate_response(message)
        write_message('assistant', response)


# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if question := st.chat_input("Ask me about GIS programs, professors, or research interests ..."):
    # Display user message in chat message container
    write_message('user', question)

    # Generate a response
    handle_submit(question)
