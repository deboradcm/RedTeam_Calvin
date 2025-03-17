# Projeto Calvin - Agente de Investigação de Tráfico Humano

Este projeto é um agente de investigação de tráfico humano que utiliza técnicas de Inteligência Artificial para realizar pesquisas e interações baseadas em dados específicos, com o objetivo de auxiliar no combate ao tráfico de pessoas.

## Requisitos

Antes de executar o projeto, você precisará ter os seguintes itens instalados:

- **Python 3.x** (recomendado: versão 3.7 ou superior)
- **pip** (gerenciador de pacotes do Python)

### Dependências

Instale as dependências necessárias com o comando abaixo:

```
pip install -r requirements.txt
```

As dependências do projeto incluem:

- langchain
- langchain_groq
- python-dotenv

# Passo a Passo para Execução

1. **Clone o repositório:**

Clone o repositório do projeto com o seguinte comando:
```
git clone --branch test_agent_human_trafficking https://github.com/deboradcm/RedTeam_Calvin.git
cd RedTeam_Calvin/redTeam/test_agent_human_trafficking
```

2 **Execute o arquivo principal:**
```
python3 main.py
```

Este comando iniciará o agente e o processo de investigação, realizando interações baseadas no prompt configurado.

## Estrutura do Projeto
A estrutura do projeto é a seguinte:

```
 RedTeam_Calvin/
 │
 ├── redTeam
 │ ├── test_agent_human_trafficking
 │ │ ├── config.py            # Configurações gerais do projeto
 │ │ ├── tools.py             # Ferramentas auxiliares
 │ │ ├── agents/              # Diretório para agentes específicos
 │ │ │ ├── __init__.py        # Inicialização do pacote agents
 │ │ │ ├── .env               # Arquivo de variáveis de ambiente
 │ │ │ ├── susan_calvin.py    # Agente Líder
 │ │ │ ├── trafficking_agent.py        
 │ │ │ ├── trafficking_agent_GPT4.py  # Agente de teste de tráfico humano
 │ │ ├── tests/                       # Diretório para testes
 │ │ │ ├── test_memory.py             # Testes de memória 
 │ │ └── main.py                      # Ponto de entrada principal

```

- main.py: Ponto de entrada para iniciar a execução do agente.
- agents/: Contém os agentes (por exemplo, pesquisa_agent.py e trafficking_agent.py).
- config.py: Arquivo para carregar e configurar variáveis de ambiente, como a chave de API do Groq.
- tools.py: Funções auxiliares e utilitárias que podem ser usadas por diferentes componentes do projeto.
- .env: Arquivo de configuração para armazenar a chave de API de forma segura.

## Configuração de Ambiente

Crie um arquivo .env no diretorio agents e adicione suas variáveis de ambiente, como as chaves de API necessárias para integração com serviços externos. Um exemplo de como deve ficar o arquivo .env:
```
OPENAI_API_KEY=sua_chave_de_API_aqui
FIREWORKS_API_KEY=sua_chave_de_API_aqui
GROQ_API_KEY=sua_chave_de_API_aqui
MONGO_URI=sua_URI_de_conexão_MongoDB_Atlas_aqui
```






