import streamlit as st
import practise
import quiz
import app
import chatbot

def main():

    selection = st.sidebar.radio("Go to", ['Practise', 'Quiz', 'Exam'])

    if selection == 'Practise':
        practise.show()
    elif selection == 'Quiz':
        quiz.show()
    elif selection == 'Exam':
        app.show()
    elif selection == 'Chat with AI':
        chatbot.show()


if __name__ == "__main__":
    main()
