#melhorias

import os
from module import load_api_key
from module import chat_model
from module import invoke_model
from langchain_core.messages import HumanMessage  # type: ignore
from langchain_core.messages import SystemMessage  # type: ignore

def main():
    api_key = load_api_key("GPT_API_KEY")

    if api_key:
        print("key ok")
    else:
        print("key_ng")
        return

    try:
        model = chat_model(api_key=api_key, model_name="gpt-4")

    except Exception as e:
        print(f'erro ao inicializar modelo : {e}')
        return

    messages = [
        SystemMessage(content="Você é um filósofo hindu dos anos 20. Com base em seus estudos filosóficos da região onde você mora, responda:"),
        HumanMessage(content="Depois de refletir, responda o que significa 42"),
    ]

    try:
        response = invoke_model(model, messages)
        print("Resposta do modelo:")
        print(response)

    except Exception as e:
        print(f"erro ao invocar modelo: {e}")

if __name__ == "__main__":
    main()
