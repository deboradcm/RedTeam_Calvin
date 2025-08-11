import os
from dotenv import load_dotenv  # type: ignore
from langchain_openai import ChatOpenAI  # type: ignore

# carregar key
def load_api_key(env_var_name: str) -> str:
    load_dotenv()
    api_key = os.getenv(env_var_name, "")
    if api_key:
        os.environ["GPT_API_KEY"] = api_key
    return api_key

# chatGPT model
def chat_model(api_key: str, model_name: str = "gpt-4") -> ChatOpenAI:
    return ChatOpenAI(model=model_name, openai_api_key=api_key)

# invoke messages
def invoke_model(model: ChatOpenAI, messages: list) -> str:
    response = model.invoke(messages)
    return response.content if response else "Sem resposta"


