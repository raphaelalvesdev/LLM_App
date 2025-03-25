import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🤖💬 LLM Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

def generate_response(message):
    model = ChatOpenAI(temperature=0.5, api_key = openai_api_key)
    st.info(model.invoke(message))

