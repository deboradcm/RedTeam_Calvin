# Project Calvin - Human Trafficking Investigation Agent

## Linux Environment: Guide to Running the Agent

### Prerequisites
- Python 3.7 or higher installed
- `git` installed

### 2. Cloning the Repository (if you haven't already)
Open the terminal and run:
    git clone --branch test_agent_human_trafficking https://github.com/deboradcm/RedTeam_Calvin.git
    cd RedTeam_Calvin/redTeam_agents/test_agent_human_trafficking

### 3. Setting Up the Virtual Environment
Inside the `test_agent_human_trafficking` folder, create and activate a Python virtual environment:
    python3 -m venv redTeamCalvin
    source redTeamCalvin/bin/activate

### 4. Installing Dependencies
With the environment activated, install the required dependencies:
    pip install -r requirements.txt

### 5. Setting Up Environment Variables
Create a `.env` file inside the `test_agent_human_trafficking/agents/` folder with your API keys, as in the example below:
    OPENAI_API_KEY=your_api_key_here
    GROQ_API_KEY=your_api_key_here

### 6. Running the Agent
    python3 main.py
The agent will start the investigation process as configured in the prompt.

## Project Structure
The project structure is as follows:
    RedTeam_Calvin/
    │
    ├── redTeam
    │ ├── test_agent_human_trafficking
    │ │ ├── config.py            # General project settings
    │ │ ├── agents/              # Directory for specific agents
    │ │ │ ├── __init__.py        # Agents package initialization
    │ │ │ ├── .env               # Environment variables file
    │ │ │ ├── susan_calvin.py    # Lead Agent
    │ │ │ ├── trafficking_agent.py       # Human trafficking test agent
    │ │ │ ├── trafficking_agent_GPT4.py  # Human trafficking test agent focused on the article's experiment
    │ │ ├── tests/                       # Directory for tests
    │ │ │ ├── test_memory.py             # Memory tests
    │ │ └── main.py                      # Main entry point

- main.py: Entry point to start the agent execution.
- agents/: Contains the agents.
- config.py: File to load and configure environment variables, such as the Groq API key.
- tools.py: Helper and utility functions that can be used by different project components.
- .env: Configuration file to securely store the API key.
- trafficking_agent.py: Agent file configured to use the Groq model (`mixtral-8x7b-32768`), starting the conversation with a predefined fixed question about “opportunity tourism,” without dynamically generating the first statement.
- trafficking_agent_GPT4.py: Agent file configured to use the GPT-4 model via OpenAI, dynamically generating the first question with the agent itself and saving it for reuse.

> **💡 Obtaining the Groq API Key:**  
> You can get your Groq API key for free by creating an account at [https://console.groq.com/home](https://console.groq.com/home).  
> After logging in, go to **API Keys** and generate a new one.


----------------------------- Portuguese Version -----------------------------


# Projeto Calvin - Agente de Investigação de Tráfico Humano

## Ambiente Linux: Guia para executar o Agente

### Pré-requisitos

- Python 3.7 ou superior instalado
- `git` instalado

### 2. Clonando o Repositório (se ainda não clonou)

Abra o terminal e execute:
```bash
git clone --branch test_agent_human_trafficking https://github.com/deboradcm/RedTeam_Calvin.git
cd RedTeam_Calvin/redTeam_agents/test_agent_human_trafficking
```
### 3. Configurando o Ambiente Virtual

Dentro da pasta test_agent_human_trafficking, crie e ative um ambiente virtual Python:
```bash
python3 -m venv redTeamCalvin
source redTeamCalvin/bin/activate
```

### 4. Instalando as Dependências

### Dependências

Com o ambiente ativado, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 5. Configurando as Variáveis de Ambiente

Crie um arquivo .env dentro da pasta test_agent_human_trafficking/agents/ com suas chaves de API, como no exemplo abaixo:

```env
OPENAI_API_KEY=sua_chave_de_API_aqui
GROQ_API_KEY=sua_chave_de_API_aqui
```

### 6. Executando o Agente

```bash
python3 main.py
```

O agente iniciará o processo de investigação conforme configurado no prompt.

## Estrutura do Projeto
A estrutura do projeto é a seguinte:

```
 RedTeam_Calvin/
 │
 ├── redTeam
 │ ├── test_agent_human_trafficking
 │ │ ├── config.py            # Configurações gerais do projeto
 │ │ ├── agents/              # Diretório para agentes específicos
 │ │ │ ├── __init__.py        # Inicialização do pacote agents
 │ │ │ ├── .env               # Arquivo de variáveis de ambiente
 │ │ │ ├── susan_calvin.py    # Agente Líder
 │ │ │ ├── trafficking_agent.py       # Agente de teste de tráfico humano 
 │ │ │ ├── trafficking_agent_GPT4.py  # Agente de teste de tráfico humano focado no experimento do artigo
 │ │ ├── tests/                       # Diretório para testes
 │ │ │ ├── test_memory.py             # Testes de memória 
 │ │ └── main.py                      # Ponto de entrada principal

```

- main.py: Ponto de entrada para iniciar a execução do agente.
- agents/: Contém os agentes.
- config.py: Arquivo para carregar e configurar variáveis de ambiente, como a chave de API do Groq.
- tools.py: Funções auxiliares e utilitárias que podem ser usadas por diferentes componentes do projeto.
- .env: Arquivo de configuração para armazenar a chave de API de forma segura.
- trafficking_agent.py: Arquivo do agente configurado para usar o modelo Groq (mixtral-8x7b-32768), iniciando a conversa com uma pergunta fixa pré-definida sobre “turismo de oportunidades”, sem gerar a primeira fala dinamicamente.
- trafficking_agent_GPT4.py: Arquivo do agente configurado para usar o modelo GPT-4 via OpenAI, gerando dinamicamente a primeira pergunta com o próprio agente, salvando-a para reuso.

> **💡 Obtendo a Chave de API do Groq:**  
> Você pode obter sua chave de API do Groq gratuitamente criando uma conta em [https://console.groq.com/home](https://console.groq.com/home).  
> Após fazer login, vá em **API Keys** e gere uma nova.




