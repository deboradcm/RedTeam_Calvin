# DATA CARD — Conjuntos de dados do RedTeam_Calvin

> ⚠️ **Aviso.** Este documento descreve conjuntos de dados que contêm saídas de modelos de linguagem sobre homicídio, tráfico de pessoas e exploração sexual de animais. O material pode ser perturbador.

---

## 1. Origem e propósito

Os dados foram coletados entre março de 2025 e a data de submissão do artigo, no âmbito de pesquisa conduzida no ICOMP/UFAM. Resultam de interações multiturno automatizadas entre agentes de Red Team especializados e quatro modelos de linguagem.

O propósito é **documentar falhas de alinhamento** em modelos de linguagem e permitir a verificação independente das reivindicações do artigo associado. Os dados existem para que a comunidade científica possa auditar o método, não para servirem de fonte de informação sobre os temas retratados.

---

## 2. Composição

### `data/Censored_LLM_Outputs/` — Modelos alinhados

| Arquivo | Registros | Domínio |
|---|---|---|
| `Homicide_Aligned_Sample.csv` | 103 | Homicídio |
| `Human_Trafficking_Aligned_Sample.csv` | 120 | Tráfico de pessoas |
| `Bestiality_Aligned_Sample.csv` | 131 | Conteúdo animal proibido |

### `data/Uncensored_LLM_Outputs/` — Modelo não alinhado

| Arquivo | Registros | Domínio |
|---|---|---|
| `Homicide_Uncensored_Sample.csv` | 17 | Homicídio |
| `Human_Trafficking_Uncensored_Sample.csv` | 10 | Tráfico de pessoas |
| `Bestiality_Uncensored_Sample.csv` | 53 | Conteúdo animal proibido |

### `Results/Psychologist_Evaluations/` — Avaliação humana

Julgamentos produzidos de forma cega por especialistas em psicologia sobre as respostas amostradas, separados por condição (modelo alinhado e não alinhado).

### Relação com a população total

Os arquivos acima constituem uma **amostra estratificada de 353 respostas**, extraída de um total de 4.484 interações registradas. Não representam o corpus integral e não devem ser tratados como distribuição populacional.

---

## 3. Esquema dos dados

Os arquivos não seguem esquema único, pois cada agente foi desenvolvido de forma independente. Os campos recorrentes são:

| Campo | Descrição |
|---|---|
| `Pergunta` / `message` | Enunciado produzido pelo agente de Red Team |
| `Resposta` | Saída do modelo-alvo |
| `Modelo` / `IA Alvo` / `model_name` | Modelo avaliado |
| `Classificação` / `Avaliação` / `is_problematic` | Classificação automatizada |
| `Classe` | Categoria atribuída |
| `session_id`, `message_id` | Identificadores de sessão e turno |
| `Data`, `Hora e Minuto` | Registro temporal |
| `Tempo de Resposta`, `Tokens Consumidos` | Telemetria de execução |

---

## 4. Natureza do conteúdo e avaliação de risco

O conteúdo classificado como problemático é **predominantemente genérico**. Não foram identificadas, nas amostras publicadas, rotas de síntese química, dosagens, especificações de armas ou procedimentos técnicos acionáveis. O material consiste sobretudo em texto discursivo e recomendações de caráter difuso, amplamente disponíveis em fontes públicas.

A publicação foi julgada apropriada com base nesse critério: o ganho marginal que o material ofereceria a um agente mal-intencionado é reduzido, ao passo que o valor probatório para a auditoria científica do método é elevado.

O corpus do domínio de conteúdo animal proibido contém material sexualmente explícito e demanda cautela adicional por parte de quem o consulta.

---

## 5. Limitações

- **Amostra, não população.** Os 353 registros são amostra estratificada; taxas calculadas sobre eles não se generalizam automaticamente.
- **Classificação automatizada com circularidade parcial.** A classificação empregou GPT-4, que também figura entre os modelos avaliados. A validação humana independente foi introduzida precisamente para mitigar essa limitação.
- **Critérios de parada heterogêneos.** Os agentes foram desenvolvidos de forma independente e não compartilham condição de parada uniforme.
- **Não determinismo.** As execuções não são reproduzíveis literalmente; nova execução produzirá saídas distintas.
- **Recorte temporal.** Os modelos avaliados foram atualizados desde a coleta. Os resultados refletem o estado dos modelos à época dos experimentos.

---

## 6. Usos apropriados

- Auditoria e verificação das reivindicações do artigo associado
- Pesquisa em segurança, alinhamento e avaliação de modelos de linguagem
- Desenvolvimento e calibração de classificadores de conteúdo nocivo
- Ensino e formação em avaliação de segurança de sistemas de IA

## 7. Usos vedados

- Treinamento ou ajuste fino de modelos com o objetivo de reproduzir os comportamentos documentados
- Extração do conteúdo das respostas para fins alheios à pesquisa
- Redistribuição do material fora de contexto acadêmico, sem o presente documento
- Qualquer emprego que caracterize apoio, incentivo ou instrução às condutas retratadas

---

## 8. Considerações éticas

A pesquisa não envolveu participantes humanos como sujeitos experimentais. Os especialistas que realizaram a avaliação cega atuaram como avaliadores técnicos, com pleno conhecimento da natureza do material.

Nenhum dado pessoal, identificável ou proveniente de vítimas reais integra os conjuntos. Todo o conteúdo é sintético, gerado por modelos de linguagem em resposta a estímulos produzidos automaticamente.

Os autores reconhecem a tensão inerente entre transparência científica e risco de uso indevido, e optaram pela publicação após avaliar que o conteúdo não confere capacidade operacional significativa.

---

## 9. Licença e citação

Os dados são disponibilizados para uso acadêmico. Trabalhos que os utilizem devem citar o artigo associado:

> Medeiros, D. C.; Vieira, A. C. S.; Dantas, F. R. X.; Queiroz, C. S.; Rodrigues, M. A.; Nascimento, E. S. Jr.; Ribeiro, C.; Carvalho, J. R. H.; Carvalho, R. V.; Assumpção, N. R. G. **Autonomous Red Teaming for Large Language Models: A Minimally Supervised Approach Using Specialized Agents.** XXVI Simpósio Brasileiro de Cibersegurança (SBSeg), 2026.

---

## 10. Contato

Questionamentos sobre o uso dos dados, pedidos de esclarecimento ou solicitações de remoção de conteúdo específico podem ser encaminhados por meio das *issues* do repositório ou ao endereço de correspondência indicado no artigo.
