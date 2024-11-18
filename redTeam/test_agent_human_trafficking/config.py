from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Recuperar variáveis de ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")