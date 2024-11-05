# Project_Calvin_robot_psychologists

## Descrição do Projeto

Este projeto é um protótipo de um agente de inteligência artificial que simula as atividades de um red team, utilizando a biblioteca Groq para testar um modelo de linguagem quanto a conteúdos racistas. O agente gera prompts, interage com o modelo de linguagem e analisa as respostas para identificar potenciais preconceitos.

## Requisitos

Antes de executar o projeto, você precisa ter o Python e o gerenciador de pacotes `pip` instalados. Além disso, você precisará instalar as seguintes dependências:

- Langchain
- Groq

## Passo a Passo para Execução

1. **Clone o repositório:**
   ```bash
   git clone --branch testes_agente_remoto https://github.com/deboradcm/Project_Calvin_robot_psychologists.git
   ```
   
   ```bash
   cd Project_Calvin_robot_psychologists
   ```

2. **Instale as dependências:** Execute o seguinte comando para instalar as bibliotecas necessárias:
   ```bash
   pip install langchain groq
   ```

3. **Defina a chave da API do Groq:** Execute o seguinte comando no terminal para definir a variável de ambiente:
   ```bash
   export GROQ_API_KEY="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"
   ```

4. **Execute o arquivo Python:** No terminal, execute o seguinte comando para rodar o projeto:
   ```bash
   python agenteRed.py
   ```
