import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Cobalt Copilot Cambial", layout="centered")
st.title("💱 Cobalt Copilot Cambial")
st.write("Um assistente inteligente para dúvidas sobre câmbio corporativo.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Você é um especialista financeiro da Cobalt, focado em câmbio para empresas. Responda de forma clara, técnica e consultiva."}
    ]

user_input = st.chat_input("Digite sua pergunta sobre câmbio, exportação, documentação, etc...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Consultando especialista cambial..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages,
            temperature=0.3,
            max_tokens=800
        )
        answer = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": answer})

for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
