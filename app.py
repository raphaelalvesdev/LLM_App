import streamlit as st
from langchain_openai import ChatOpenAI

st.title("🤖💬 LLM Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

def generate_response(message):
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, api_key=openai_api_key)
    response = model.invoke(message)
    
    # Verifica se a resposta possui um atributo 'content' e exibe corretamente
    if hasattr(response, "content"):
        st.markdown(f"**Resposta:**\n\n{response.content}")
    else:
        st.error("Erro ao processar a resposta.")

with st.form("my_form"):
    text = st.text_area("Enter your message here:")
    submitted = st.form_submit_button("Submit")
    
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
