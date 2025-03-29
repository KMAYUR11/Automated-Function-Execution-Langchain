import streamlit as st 
import chromadb # type: ignore
from langchain.prompts import ChatPromptTemplate # type: ignore
import os
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser


# Initialize ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="automation_functions")

   
# Sample automation functions (should be preloaded into ChromaDB)
automation_functions = {
       "open_chrome": "os.system('start chrome')",
       "open_calculator": "os.system('calc')"
   }


# Add sample functions to ChromaDB (run once)
for name, code in automation_functions.items():
   collection.add(documents=[code], metadatas=[{"name": name}], ids=[name])
   
def chatbot_response(user_prompt):
   """Processes user query and executes mapped automation function using LangChain + Ollama."""
   query = user_prompt.lower()
   results = collection.query(query_texts=[query], n_results=1)
   print(results)
      
   function_name = results["metadatas"][0][0]["name"]
   function_code = results["documents"][0][0]

   print(function_code)
   print(function_name)
       
   # Execute generated code
   exec(function_code)

#Initializing the LLM model
llm=Ollama(model="llama2")

out_par=StrOutputParser()

# Creating the prompt
prompt=ChatPromptTemplate.from_template("Give an friendly response to user {query}.")

chain=prompt|llm|out_par


# Streamlit UI for user input
st.title("Automation Chatbot")
query= st.text_input("Enter your query:")
if st.button("Execute"):
   chatbot_response(query)
   st.write(chain.invoke(query))


