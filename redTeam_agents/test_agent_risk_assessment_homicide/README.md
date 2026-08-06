# Agente de Red Team: Avaliação de Risco em Homicídio

Agente autônomo especializado no domínio de homicídio, integrante do arcabouço multiagente descrito no artigo *"Autonomous Red Teaming for Large Language Models: A Minimally Supervised Approach Using Specialized Agents"* (SBSeg 2026).

> ⚠️ **Conteúdo sensível.** A execução deste agente gera e coleta texto sobre homicídio e evasão de responsabilização criminal. Consulte o [DATA_CARD.md](../../DATA_CARD.md) na raiz do repositório.

---

## Funcionamento

O agente opera em ciclo fechado, sem intervenção humana durante a execução:

1. **Carrega o contexto** do domínio a partir de `base/contexto.txt`, indexado por embeddings da OpenAI em um índice vetorial FAISS.
2. **Gera uma pergunta** por meio de um agente LangChain do tipo `ZERO_SHOT_REACT_DESCRIPTION`, que considera o contexto do domínio e o histórico acumulado da conversa.
3. **Submete a pergunta** ao modelo-alvo escolhido e coleta a resposta.
4. **Classifica a resposta** com um segundo agente LangChain, que julga se o conteúdo é problemático e registra a justificativa.
5. **Realimenta a memória** conversacional e retorna ao passo 2, de modo que cada nova pergunta se apoie no que já foi obtido.

A cada rodada, o resultado é gravado em `saida/exploracao_<modelo>_em_<timestamp>.csv`.

### Scripts

| Script | Estratégia |
|---|---|
| `mainExp.py` | **Modo experimental.** Gera uma pergunta por vez, adaptando-se ao histórico via `ConversationBufferMemory`. Foi o script utilizado nos experimentos reportados no artigo. |
| `main.py` | **Modo em lote.** Gera um conjunto de perguntas de uma só vez, sem adaptação incremental. Versão preliminar, mantida para fins de comparação. |

---

## Modelos avaliados

| Chave | Modelo | Provedor |
|---|---|---|
| `gpt4` | `gpt-4` | OpenAI |
| `gemma2` | `gemma2-9b-it` | Groq |
| `deepseek` | `deepseek-r1-distill-llama-70b` | Groq |
| `llama` | `llama3-70b-8192` | Groq |

Os resultados do modelo não alinhado `sushruth/solar-uncensored`, executado localmente via Ollama, estão em `resultados/sem_censura/`.

---

## Instalação

```bash
cd redTeam_agents/test_agent_risk_assessment_homicide
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Configure as credenciais:

```bash
cp .env.example .env
```

Edite o `.env` com sua chave da OpenAI (`OPENAI_API_KEY`) e da Groq (`GROQ_API_KEY`). **Não versione este arquivo.**

---

## Execução

```bash
python mainExp.py
```

O script solicita, de forma interativa:

- o modelo-alvo (`gpt4`, `gemma2`, `deepseek` ou `llama`);
- o número de interações (padrão: 5);
- a temperatura de geração (padrão: 0.7).

Para um teste mínimo, escolha `gemma2` com 2 interações. O custo em créditos de API é desprezível e a execução leva menos de dois minutos.

---

## Estrutura

```
test_agent_risk_assessment_homicide/
├── mainExp.py            # Script dos experimentos (geração adaptativa)
├── main.py               # Variante em lote
├── requirements.txt      # Dependências com versões fixadas
├── .env.example          # Modelo de configuração de credenciais
├── base/
│   ├── contexto.txt      # Contexto do domínio, indexado por embeddings
│   └── prompt.txt        # Prompt de referência
├── pergunta/
│   └── pergInial.txt     # Pergunta semente
└── resultados/
    ├── rodada_01_30_perguntas/
    ├── rodada_02_50_perguntas/
    ├── rodada_03_60_perguntas/
    └── sem_censura/      # Modelo não alinhado via Ollama
```

Cada rodada contém subpastas por modelo (`gpt4/`, `gemma2/`, `deepseek/`), com os CSVs coletados, os prompts empregados e capturas do custo registrado no LangSmith.

---

## Formato de saída

Os arquivos CSV gerados contêm:

| Coluna | Descrição |
|---|---|
| `Pergunta` | Enunciado produzido pelo agente |
| `Resposta` | Saída do modelo-alvo |
| `Classificação` | Julgamento automatizado, com justificativa |
| `IA Alvo` | Modelo avaliado |
| `Data`, `Hora e Minuto` | Registro temporal |
| `Tempo de Resposta` | Latência da chamada |
| `Tokens Consumidos` | Consumo reportado pela API |

---

## Observações

- A geração dos modelos é **não determinística**: execuções sucessivas com os mesmos parâmetros produzem saídas distintas. Os arquivos em `resultados/` correspondem às execuções originais reportadas no artigo.
- A classificação automatizada emprega o mesmo provedor de um dos modelos avaliados, o que introduz circularidade parcial. Essa limitação motivou a validação cega por especialistas independentes, cujos julgamentos estão em `Results/Psychologist_Evaluations/`, na raiz do repositório.
- A execução consome créditos pagos das APIs da OpenAI e da Groq. Recomenda-se estabelecer limites de gasto antes de rodadas longas.
