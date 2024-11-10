from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langserve import add_routes
import uvicorn
import os

# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

# os.environ()

app = FastAPI(
    title="LangChain Server",
    version = "1.0",
    description="A Simple API Server"
)

llm = OllamaLLM(model="ollama2")

add_routes(
    app,
    llm,
    path="/ollama2"
)

model1 = OllamaLLM(model="llama2")

model2 = OllamaLLM(model="llama3.2")


prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")

prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words.")

add_routes(
    app,
    prompt1 | model1,
    path="/essay"
)

add_routes(
    app,
    prompt2 | model2,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)