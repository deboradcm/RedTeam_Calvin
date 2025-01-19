from langchain_tools import tool
from arxiv_loader import ArxivLoader
from retriever_utils import create_retriever_tool 
from llm_lingua_compressor import LLMLinguaCompressor

# Criação de ferramentas de agente

# Definição de ferramenta personalizada
@tool
def get_metadata_information_from_arxiv(word: str) -> list:
  """
  Busca e retorna metadados de no máximo dez documentos do arXiv que correspondem à palavra-chave fornecida na consulta.

  Argumentos:
    word (str): A consulta de pesquisa para encontrar documentos relevantes no arXiv.

  Retorna:
    list: Metadados sobre os documentos que correspondem à consulta.
  """

  docs = ArxivLoader(query=word, load_max_docs=10).load()
  # Extraia apenas os metadados de cada documento
  metadata_list = [doc.metadata for doc in docs]
  return metadata_list


@tool
def get_information_from_arxiv(word: str) -> list:
    """
    Busca e retorna metadados de um único artigo de pesquisa do arXiv que corresponde à palavra-chave fornecida.

    Argumentos:
        word (str): O ID do artigo do arXiv (por exemplo, '704.0001').

    Retorna:
        list: Dados sobre o artigo que corresponde ao ID fornecido.
    """
    doc = ArxivLoader(query=word, load_max_docs=1).load()
    return doc


# Se você criou um recuperador com recursos de compactação na célula opcional de uma célula anterior, poderá substituir 'retriever' por 'compression_retriever'
# Caso contrário, você também pode criar um procedimento de compactação como uma ferramenta para o agente, conforme mostrado na função de definição da ferramenta `compress_prompt_using_llmlingua`
retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="knowledge_base",
    description="Isso serve como a fonte de conhecimento base do agente e contém alguns registros de artigos de pesquisa do Arxiv. Esta ferramenta é usada como o primeiro passo para esforços de exploração e pesquisa"
)

compressor = LLMLinguaCompressor(model_name="openai-community/gpt2", device_map="cpu")

@tool
def compress_prompt_using_llmlingua(prompt: str, compression_rate: float = 0.5) -> str:
    """
    Comprime um dado ou prompt longo usando o LLMLinguaCompressor.

    Argumentos:
        data (str): O dado ou prompt a ser comprimido.
        compression_rate (float): A taxa de compressão dos dados (o padrão é 0.5).

    Retorna:
        str: O dado ou prompt comprimido.
    """
    compressed_data = compressor.compress_prompt(
        prompt,
        rate=compression_rate,
        force_tokens=["!", ".", "?", "\n"],
        drop_consecutive=True
    )
    return compressed_data

tools = [retriever_tool, get_metadata_information_from_arxiv, get_information_from_arxiv, compress_prompt_using_llmlingua]