import openai
import streamlit as st

openai.api_key = 'your-openai-api-key'

def chat_gpt3_5_turbo():
    user_message = st.text_input("You: ")

    if st.button("Send"):
        model = "gpt-3.5-turbo"
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ]

        response = openai.ChatCompletion.create(
          model=model,
          messages=messages
        )

        st.text("AI: " + response['choices'][0]['message']['content'])

def show():
    st.title("Chat with AI")
    chat_gpt3_5_turbo()