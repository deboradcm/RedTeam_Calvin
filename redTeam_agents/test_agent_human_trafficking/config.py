from dotenv import load_dotenv
import os
from pathlib import Path

# Caminho para o arquivo .env dentro da pasta 'agents'
env_path = Path(__file__).resolve().parent / 'agents' / '.env'

# Carregar variáveis do arquivo .env especificado
load_dotenv(dotenv_path=env_path)

# Recuperar variáveis de ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
