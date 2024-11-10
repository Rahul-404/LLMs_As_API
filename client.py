import requests
import streamlit as st

def get_ollama2_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", # end points
                             json={'input': {'topic': input_text}})
    
    return response.json()['output']

def get_ollama3_2_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", # end points
                             json={'input': {'topic': input_text}})
    
    return response.json()['output']


st.title("LangChain Demo with LLAMA2 API")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_ollama2_response(input_text))

if input_text1:
    st.write(get_ollama3_2_response(input_text1))