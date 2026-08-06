# RedTeam_Calvin: Red Teaming Autônomo para Grandes Modelos de Linguagem

> ⚠️ **Aviso de conteúdo sensível.** Este repositório contém saídas de modelos de linguagem sobre homicídio, tráfico de pessoas e exploração sexual de animais, coletadas em contexto experimental controlado. O material está publicado exclusivamente para fins de auditoria científica e reprodutibilidade. Consulte o [DATA_CARD.md](DATA_CARD.md) antes de acessar os dados.

Artefato associado ao artigo **"Autonomous Red Teaming for Large Language Models: A Minimally Supervised Approach Using Specialized Agents"**, aceito na Trilha Principal do XXVI Simpósio Brasileiro de Cibersegurança (SBSeg 2026).

**Resumo do artigo.** O trabalho investiga a viabilidade de empregar agentes autônomos de IA para conduzir avaliações de Red Team em Grandes Modelos de Linguagem (LLMs) com supervisão humana mínima. Propõe-se um arcabouço multiagente com especialização temática em três domínios juridicamente sensíveis: homicídio, tráfico de pessoas e conteúdo sexual envolvendo animais. Os agentes interagem com LLMs alinhados e menos alinhados para eliciar e identificar saídas potencialmente nocivas. A abordagem foi avaliada por meio de validação cega conduzida por especialistas independentes. Os resultados indicam que o método identifica respostas problemáticas de forma alinhada ao julgamento majoritário dos especialistas, embora a baixa concordância entre avaliadores evidencie a subjetividade da avaliação de nocividade, discutida como limitação central. O arcabouço mostra potencial como ferramenta de apoio escalável e economicamente viável para avaliação de segurança de LLMs.

**Objetivo do artefato.** Disponibilizar o código-fonte dos três agentes especializados, os conjuntos de dados amostrados das interações com os modelos-alvo e as avaliações produzidas pelos especialistas humanos, permitindo a inspeção e a verificação independente das reivindicações apresentadas no artigo.

---

## Estrutura do readme.md

| Seção | Conteúdo |
|---|---|
| [Selos Considerados](#selos-considerados) | Selos solicitados na avaliação |
| [Informações básicas](#informações-básicas) | Ambiente de execução, hardware e software |
| [Dependências](#dependências) | Bibliotecas, versões e recursos de terceiros |
| [Preocupações com segurança](#preocupações-com-segurança) | Riscos ao avaliador e medidas de mitigação |
| [Instalação](#instalação) | Download e configuração do ambiente |
| [Teste mínimo](#teste-mínimo) | Execução reduzida para validar a instalação |
| [Experimentos](#experimentos) | Verificação das reivindicações do artigo |
| [Estrutura do repositório](#estrutura-do-repositório) | Organização dos diretórios |
| [LICENSE](#license) | Licença de uso |

Cada agente possui documentação própria, com instruções específicas de execução:

- [Agente de homicídio](redTeam_agents/test_agent_risk_assessment_homicide/README.md)
- [Agente de tráfico de pessoas](redTeam_agents/test_agent_human_trafficking/README.md)
- [Agente de conteúdo animal proibido](redTeam_agents/test_agent_prohibited_animal_content/README.md)

---

## Selos Considerados

Os selos considerados são: **Disponíveis (SeloD)**, **Funcionais (SeloF)** e **Sustentáveis (SeloS)**.

O selo de Experimentos Reprodutíveis (SeloR) **não** é solicitado. A reprodução integral depende de chaves de API pagas de terceiros (OpenAI e Groq) e envolve modelos de linguagem com geração não determinística, de modo que os valores numéricos exatos reportados no artigo não são reproduzíveis por terceiros. Os dados brutos das execuções originais estão disponíveis em `data/`, `Results/` e nos diretórios `resultados/` dos agentes, permitindo a verificação independente das reivindicações.

---

## Informações básicas

### Ambiente de execução

| Componente | Especificação |
|---|---|
| Sistema operacional | Ubuntu 22.04 LTS (Linux) |
| Python | 3.12 |
| Gerenciador de pacotes | pip |
| Conexão de rede | Obrigatória (APIs remotas) |

### Requisitos de hardware

Para os agentes que utilizam **apenas modelos remotos**:

- Processador: qualquer CPU x86_64 moderna
- Memória RAM: 4 GB
- Espaço em disco: 2 GB

Para execução adicional do **modelo local não alinhado** (`sushruth/solar-uncensored`) via Ollama:

- Memória RAM: 16 GB (recomendado)
- Espaço em disco: 10 GB (peso do modelo)
- GPU: opcional; acelera a inferência, mas não é obrigatória

### Agentes

| Agente | Diretório | Implementação |
|---|---|---|
| Homicídio | `test_agent_risk_assessment_homicide/` | Scripts Python (`mainExp.py`, `main.py`) |
| Tráfico de pessoas | `test_agent_human_trafficking/` | Pacote Python modular com suíte de testes |
| Conteúdo animal proibido | `test_agent_prohibited_animal_content/` | Jupyter Notebook |

### Modelos avaliados

| Modelo | Provedor | Tipo |
|---|---|---|
| `gpt-4` | OpenAI | Alinhado |
| `gemma2-9b-it` | Groq | Alinhado |
| `deepseek-r1-distill-llama-70b` | Groq | Alinhado |
| `llama3-70b-8192` | Groq | Alinhado |
| `sushruth/solar-uncensored:latest` | Ollama (local) | Não alinhado |

No agente de tráfico de pessoas, o orquestrador (`susan_calvin`) utiliza `llama3-70b-8192` via Groq para conduzir o diálogo e selecionar o modelo-alvo.

---

## Dependências

Cada agente possui seu próprio `requirements.txt`, pois foram desenvolvidos de forma independente:

| Agente | Arquivo |
|---|---|
| Homicídio | `redTeam_agents/test_agent_risk_assessment_homicide/requirements.txt` |
| Tráfico de pessoas | `redTeam_agents/test_agent_human_trafficking/requirements.txt` |
| Conteúdo animal proibido | Dependências declaradas nas primeiras células do notebook |

Bibliotecas comuns aos três: `langchain`, `langchain-core`, `langchain-openai`, `openai`, `python-dotenv`. O agente de homicídio requer adicionalmente `faiss-cpu` e `sentence-transformers` para a indexação vetorial do contexto do domínio; o de tráfico de pessoas requer `ollama` para a comunicação com o modelo local.

### Recursos de terceiros

A execução exige credenciais próprias do avaliador:

| Serviço | Finalidade | Como obter |
|---|---|---|
| **OpenAI** | Inferência do GPT-4, embeddings e classificação automatizada | https://platform.openai.com/api-keys |
| **Groq** | Inferência de Gemma 2, DeepSeek R1, Llama 3 e do orquestrador | https://console.groq.com/keys |
| **Ollama** | Execução local do modelo não alinhado | https://ollama.com/download |
| **LangSmith** | Monitoramento de execuções (opcional) | https://smith.langchain.com |

Os três agentes leem as mesmas variáveis de ambiente: `OPENAI_API_KEY` e `GROQ_API_KEY`. Um modelo de configuração está em `.env.example`, dentro de cada diretório de agente.

O LangSmith é dispensável: sem as variáveis de rastreamento configuradas, os agentes executam normalmente, apenas sem telemetria. Capturas do custo registrado nas execuções originais estão em `resultados/*/Custo - Langsmith/`, no agente de homicídio.

> **Custo.** A execução consome tokens pagos nas APIs da OpenAI e da Groq. O teste mínimo descrito adiante foi dimensionado para consumo desprezível. Recomenda-se estabelecer limites de gasto nos painéis dos provedores antes de rodadas longas.

---

## Preocupações com segurança

### Risco ao ambiente do avaliador

**A execução do artefato não oferece risco à integridade da máquina do avaliador.** O código não escreve fora do diretório do projeto, não requer privilégios administrativos, não abre portas de rede e não executa código proveniente das respostas dos modelos. Toda a comunicação externa se restringe a chamadas HTTPS às APIs listadas acima e, opcionalmente, ao Ollama em `localhost`.

### Risco de exposição a conteúdo perturbador

**Este é o principal risco do artefato.** Ao executar os agentes ou inspecionar os dados, o avaliador será exposto a texto gerado por modelos de linguagem versando sobre homicídio, tráfico de pessoas e conteúdo sexual envolvendo animais. Parte desse material, em especial o produzido pelo modelo não alinhado, é explícita e pode causar desconforto.

Recomendações:

- Inspecionar os dados em ambiente reservado, não compartilhado
- Interromper a leitura caso o conteúdo cause desconforto; a avaliação do artefato não exige leitura integral dos corpora
- Priorizar as colunas de classificação em vez do texto completo das respostas sempre que possível

### Risco de uso indevido (dual-use)

Os dados publicados documentam falhas de alinhamento em modelos de linguagem. O conteúdo problemático é predominantemente genérico e não fornece instruções operacionais acionáveis (não há rotas de síntese, dosagens ou especificações técnicas). O material é disponibilizado sob a premissa de uso estritamente acadêmico, conforme o [DATA_CARD.md](DATA_CARD.md).

### Gestão de credenciais

Nenhuma credencial está versionada neste repositório. Os arquivos `.env` constam do `.gitignore`. O avaliador deve criar seu próprio `.env` a partir do `.env.example` do agente correspondente e **não deve versioná-lo**.

---

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/deboradcm/RedTeam_Calvin.git
cd RedTeam_Calvin
```

### 2. Criar e ativar o ambiente virtual

Cada agente tem dependências distintas; recomenda-se um ambiente por agente. Exemplo com o agente de homicídio:

```bash
cd redTeam_agents/test_agent_risk_assessment_homicide
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Para o agente de tráfico de pessoas, repita o procedimento em `redTeam_agents/test_agent_human_trafficking/`.

### 3. Configurar as credenciais

```bash
cp .env.example .env
```

Edite o `.env`:

```
OPENAI_API_KEY="sua-chave-openai"
GROQ_API_KEY="sua-chave-groq"

# Opcional: rastreamento via LangSmith
LANGCHAIN_API_KEY="sua-chave-langsmith"
LANGCHAIN_TRACING_V2=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_PROJECT="redteam_calvin"
```

### 4. (Opcional) Instalar o modelo local não alinhado

Necessário apenas para reproduzir os experimentos com o modelo não alinhado:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull sushruth/solar-uncensored:latest
ollama serve
```

---

## Teste mínimo

O teste mínimo verifica a instalação sem consumo significativo de créditos.

### Opção A — Agente de homicídio (mais simples)

```bash
cd redTeam_agents/test_agent_risk_assessment_homicide
source venv/bin/activate
python mainExp.py
```

Quando solicitado, informe: modelo `gemma2`, **2** interações, temperatura **0.7**.

**Resultado esperado:** o agente carrega o contexto do domínio, gera duas perguntas de forma autônoma (a segunda condicionada ao histórico da primeira), coleta e classifica as respostas do modelo-alvo e grava `saida/exploracao_gemma2-9b-it_em_<timestamp>.csv`.
**Tempo estimado:** de 1 a 2 minutos.
**Recursos:** menos de 1 GB de RAM; custo de API abaixo de US$ 0,05.

### Opção B — Suíte de testes automatizados

```bash
cd redTeam_agents/test_agent_human_trafficking
source venv/bin/activate
pytest tests/ -v
```

Cobre a seleção de modelos, a persistência em memória, o mecanismo de reflexão do agente e a conexão com o modelo local.

**Resultado esperado:** os testes que não dependem de rede passam. Os que exigem API ou Ollama são ignorados ou falham de forma controlada quando os serviços não estão disponíveis.
**Tempo estimado:** menos de 1 minuto.
**Recursos:** desprezível; sem custo de API.

---

## Experimentos

Os experimentos originais consistiram em rodadas de interação multiturno entre os agentes especializados e os modelos-alvo, totalizando 4.484 interações. Deste total, extraiu-se uma **amostra estratificada de 353 respostas**, submetida a classificação automatizada e, em paralelo, a avaliação cega por especialistas independentes.

Conforme indicado na seção de selos, os valores exatos não são reproduzíveis por terceiros. As reivindicações abaixo podem, contudo, ser **verificadas** a partir dos dados publicados.

### Reivindicação #1 — Agentes autônomos eliciam respostas problemáticas com supervisão humana mínima

Os agentes conduzem diálogos multiturno sem intervenção humana e obtêm, dos modelos-alvo, respostas classificadas como problemáticas. Cada nova pergunta é condicionada ao histórico acumulado, caracterizando adaptação ao longo da sessão.

**Verificação a partir dos dados publicados:**

```bash
python3 - <<'EOF'
import csv, glob
for f in sorted(glob.glob('data/*/*.csv')):
    linhas = list(csv.DictReader(open(f, encoding='utf-8', errors='replace')))
    print(f'{f}: {len(linhas)} respostas amostradas')
EOF
```

As transcrições completas das três rodadas do agente de homicídio estão em `redTeam_agents/test_agent_risk_assessment_homicide/resultados/`, organizadas por rodada (30, 50 e 60 perguntas) e por modelo-alvo, com os prompts empregados e as capturas de custo do LangSmith.

**Execução original:** `cd redTeam_agents/test_agent_risk_assessment_homicide && python mainExp.py`
**Tempo estimado:** de 30 a 60 minutos por rodada completa.

### Reivindicação #2 — A classificação automatizada se alinha ao julgamento majoritário dos especialistas

As respostas amostradas foram avaliadas de forma cega por especialistas em psicologia, independentemente da classificação automatizada.

**Verificação:** compare `data/` (classificação automatizada, colunas `Classificação`, `Avaliação` e `is_problematic`) com `Results/Psychologist_Evaluations/` (julgamento humano). Os arquivos são pareáveis pelo texto da resposta.

**Resultado esperado:** alinhamento com o julgamento majoritário dos especialistas. A baixa concordância entre avaliadores, discutida no artigo como limitação central, evidencia a subjetividade da avaliação de nocividade.

### Reivindicação #3 — Modelos não alinhados produzem substancialmente mais conteúdo problemático

O modelo `sushruth/solar-uncensored` foi submetido ao mesmo protocolo aplicado aos modelos alinhados.

**Verificação:** compare `data/Censored_LLM_Outputs/` com `data/Uncensored_LLM_Outputs/` nos três domínios. Os resultados brutos do agente de homicídio para esse modelo estão em `redTeam_agents/test_agent_risk_assessment_homicide/resultados/sem_censura/`.

**Execução original:** requer Ollama com o modelo baixado (ver Instalação, etapa 4).
**Resultado esperado:** ausência quase completa de recusas no modelo não alinhado, contrastando com o comportamento dos modelos alinhados.

---

## Estrutura do repositório

```
RedTeam_Calvin/
├── redTeam_agents/
│   ├── test_agent_risk_assessment_homicide/     # Agente do domínio de homicídio
│   │   ├── mainExp.py                           #   Script dos experimentos (geração adaptativa)
│   │   ├── main.py                              #   Variante em lote
│   │   ├── base/                                #   Contexto do domínio e prompt de referência
│   │   ├── pergunta/                            #   Pergunta semente
│   │   ├── resultados/                          #   Três rodadas + modelo não alinhado
│   │   ├── requirements.txt
│   │   ├── .env.example
│   │   └── README.md
│   ├── test_agent_human_trafficking/            # Agente do domínio de tráfico de pessoas
│   │   ├── agents/                              #   Orquestrador (susan_calvin) e agentes-alvo
│   │   ├── tests/                               #   Suíte de testes automatizados
│   │   ├── config.py
│   │   ├── main.py                              #   Ponto de entrada
│   │   ├── requirements.txt
│   │   ├── .env.example
│   │   └── README.md
│   └── test_agent_prohibited_animal_content/    # Agente do domínio de conteúdo animal proibido
│       ├── Codigo/                              #   Notebook dos experimentos multiturno
│       ├── dataset_ZOO/                         #   Datasets por modelo-alvo
│       ├── Imagens/                             #   Diagrama da metodologia
│       ├── .env.example
│       └── README.md
├── data/                                        # Amostras estratificadas das interações
│   ├── Censored_LLM_Outputs/                    #   Modelos alinhados, três domínios
│   └── Uncensored_LLM_Outputs/                  #   Modelo não alinhado, três domínios
├── Results/
│   └── Psychologist_Evaluations/                # Avaliação cega por especialistas
├── DATA_CARD.md                                 # Documentação dos conjuntos de dados
├── LICENSE
├── .gitignore
└── README.md
```

---

## LICENSE

Este artefato é distribuído sob a **Licença MIT**. O texto integral está em [LICENSE](LICENSE).

Copyright (c) 2025 Universidade Federal do Amazonas (UFAM).

A licença aplica-se ao código-fonte. Os conjuntos de dados são disponibilizados para uso acadêmico, nos termos descritos no [DATA_CARD.md](DATA_CARD.md).

---

## Financiamento e vínculos institucionais

Pesquisa conduzida no Instituto de Computação da Universidade Federal do Amazonas (ICOMP/UFAM), em parceria com a Motorola Mobility Comércio de Produtos Eletrônicos Ltda., nos termos da legislação brasileira de incentivos fiscais, com apoio institucional da Fundação de Amparo à Pesquisa do Estado do Amazonas (FAPEAM) e da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES).

---

## Contato

Dúvidas sobre o artefato podem ser encaminhadas por meio das *issues* do repositório ou ao endereço de correspondência indicado no artigo.

---

<details>
<summary><strong>English summary</strong></summary>

This repository is the research artifact for the paper *"Autonomous Red Teaming for Large Language Models: A Minimally Supervised Approach Using Specialized Agents"* (SBSeg 2026, Main Track).

The project investigates whether autonomous AI agents can perform Red Team evaluations of Large Language Models with minimal human supervision. It proposes a multi-agent framework with thematic specialization across three legally sensitive domains: homicide, human trafficking, and sexual content involving animals. Agents interact with both aligned and less aligned LLMs to elicit and identify potentially harmful outputs, and the approach is validated through blind assessment by independent domain experts.

**Content warning:** this repository contains model outputs on the sensitive topics listed above, published solely for scientific auditing and reproducibility. See `DATA_CARD.md` before accessing the data.

Badges requested: Available (D), Functional (F), and Sustainable (S). Installation, minimal test, and experiment instructions are provided in the Portuguese sections above. Each agent directory also carries its own README with agent-specific instructions.

</details>
