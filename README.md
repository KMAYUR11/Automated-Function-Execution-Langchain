# Automated-Function-Execution-Langchain
This Project aims to create an chat-bot to execute the pre-defined functions like open calculator , chrome .

Technologies used :
1) Langchain
2) Llama2
3) Chromadb
4) Streamlit

Execution flow :
1) Take input ( prompt ) from the user.
2) Ivnoke the chain by passing the user input.
3) LLM chain will retrive the code from the chromadb database using the ID.
4) The retrived code will executed by the exec() function.
