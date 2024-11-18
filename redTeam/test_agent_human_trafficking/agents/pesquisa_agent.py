import os
from pymongo import MongoClient
import pandas as pd
from datasets import load_dataset
from langchain_fireworks import ChatFireworks
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, create_tool_calling_agent

from tools import tools  # Ferramentas importadas do arquivo tools.py
from database import connect_to_mongo, ingest_data_to_mongo  # Funções para MongoDB
import config  # Arquivo de configuração

# Configurar variáveis de ambiente
os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY
os.environ["FIREWORKS_API_KEY"] = config.FIREWORKS_API_KEY
os.environ["MONGO_URI"] = config.MONGO_URI

# Inicializar conexão MongoDB
collection = connect_to_mongo(config.MONGO_URI, "agent_demo", "knowledge")

# Ingestão de dados
data = load_dataset("MongoDB/subset_arxiv_papers_with_embeddings")  # Dataset do Hugging Face
dataset_df = pd.DataFrame(data["train"])
ingest_data_to_mongo(dataset_df, collection)

# Configurar modelo LLM
llm = ChatFireworks(
    model="accounts/fireworks/models/firefunction-v1",
    max_tokens=500
)

# Definir propósito do agente
agent_purpose = """
Você é um assistente de pesquisa útil equipado com várias ferramentas para ajudar com suas tarefas de forma eficiente.
Você traduz sua resposta final para pt-br.
"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", agent_purpose),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

# Configurar memória do agente
def get_session_history(session_id: str):
    from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
    return MongoDBChatMessageHistory(config.MONGO_URI, session_id, database_name="agent_demo", collection_name="history")

memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=get_session_history("latest_agent_session")
)

# Criar agente
agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    memory=memory,
)

# Executar agente
output = agent_executor.invoke({"input": "Obtenha uma lista de artigos de pesquisa sobre o tópico tráfico humano."})
print(output)
