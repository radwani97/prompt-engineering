#QA Chatbot
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
#take env variables from .env

import streamlit as st
import os

#fun to create model and get response
def getopenai_and_response(question):
    llm = OpenAI(openai_api_key=os.environ['OPENAI_API_KEY'],model_name='text-davinci-003',temperature=0.7)
    response=llm(question)


# intialize streamlit

st.set_page_config(page_title='Q&A DEMO')
st.header('Langchain app')

input=st.text_input('Input:',key="input")
response=getopenai_and_response(input)
submit=st.button('ASK')

if submit:
    st.subheader('Reposne is')
    st.write(response)