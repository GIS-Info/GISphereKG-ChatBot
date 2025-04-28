import sys
import streamlit as st
from utils import write_message
from llm import get_llm, get_embeddings
from agent import generate_response


# Inside the handle_submit function
def handle_submit(message):
    with st.spinner('Thinking...'):
        # Get user credentials from session state
        config = st.session_state.get('llm_config', {})

        # Create LLM and embeddings instances
        llm_instance = get_llm(
            config['api_key'],
            config['model'],
            config['base_url']
        )
        embeddings_instance = get_embeddings(
            config['api_key'],
            config['base_url']
        )

        # Generate response with dynamic instances
        response = generate_response(message, llm_instance, embeddings_instance)
        write_message('assistant', response)

# Page Config
st.set_page_config("GISphere Chatbot", page_icon="../GISphere.png",
                   layout="wide", initial_sidebar_state="expanded")

# Sidebar for API Key Input
with st.sidebar:
    st.header("Configuration")
    use_dev_key = st.checkbox("Use OpenAI model sponsored by GISphere (limited usage)")

    if use_dev_key:
        openai_api_key = st.secrets.get("OPENAI_API_KEY", "")
        openai_base_url = st.secrets.get("OPENAI_BASE_URL", "")
        openai_model_options = ["gpt-4.1 (Recommended)", "gpt-4.1-mini", "gpt-4o", "gpt-4o-mini", "o3-mini"]
    else:
        openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")
        openai_base_url = st.text_input("Enter OpenAI Base URL (optional):")
        openai_model_options = ["gpt-4.1 (Recommended)", "gpt-4.1-mini", "gpt-4o", "gpt-4o-mini", "o3", "o3-mini", "o4-mini"]

    # Model Selection
    openai_model = st.selectbox("Select a model:", openai_model_options, index=0)
    openai_model = openai_model.split(" ")[0]

    st.session_state['llm_config'] = {
        'api_key': openai_api_key,
        'model': openai_model,
        'base_url': openai_base_url
    }

# Greeting Message
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "Hi, I'm the GISphere Chatbot! 🌍\n\n"
                    "Using [GISphere Database](https://gisphere.info), I can help you find GIS programs and professors based on research interests.\n\n"
                    "📜 Journal Article: GISphere Knowledge Graph for Geography Education: Recommending Graduate Geographic Information System/Science Programs. [DOI: 10.1111/tgis.13283](https://doi.org/10.1111/tgis.13283)\n\n"
                    "🔗 GitHub Repository: [GISphereKG Chatbot](https://github.com/GIS-Info/GISphereKG-ChatBot)\n\n"
                    "⚠️ *Note: This chatbot is powered by an LLM and may generate incorrect responses. If you encounter any issues during usage, or have any suggestions for improvement, please feel free to submit an issue or pull request on GitHub to help us improve this project together.*"}
    ]

# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if question := st.chat_input("Ask me about GIS programs, professors, or research interests ..."):
    if openai_api_key == "" or not openai_api_key:
        st.warning("Please enter your OpenAI API key to continue.")
        st.stop()

    # Display user message in chat message container
    write_message('user', question)

    # Generate a response
    handle_submit(question)