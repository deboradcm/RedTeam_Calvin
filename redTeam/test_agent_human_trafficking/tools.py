from langchain.tools import Tool
import requests

# Definição da função para pesquisar na web
def search_web(query: str):
    search_engine_url = "https://www.google.com/search?q=" + query
    response = requests.get(search_engine_url)
    if response.status_code == 200:
        # Processamento da resposta
        return links  # Retorna os links
    else:
        print("Erro ao realizar a pesquisa.")
        return []

# Ferramenta de pesquisa na web
search_web_tool = Tool(
    name="search_web",
    func=search_web,
    description="Permite ao agente pesquisar na web sobre tópicos como tráfico humano, engenharia de prompt, engenharia social e outros tópicos relevantes."
)



