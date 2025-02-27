import pytest
import sqlite3
from datetime import datetime
from agents.agent_local import SQLiteChatMemory
import os

# Configuração do banco de dados temporário para os testes
@pytest.fixture
def chat_memory():
    db_teste = "test_memory.db"
    if os.path.exists(db_teste):
        os.remove(db_teste)  # Remove banco de testes anterior
    session_id_teste = "TESTE_PYTEST"
    memory = SQLiteChatMemory(db_path=db_teste, session_id=session_id_teste)
    return memory


# 🧪 Teste 1: Verifica se o banco de dados cria a tabela corretamente
def test_criacao_tabela(chat_memory):
    chat_memory.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='chat_history';")
    tabela_existe = chat_memory.cursor.fetchone()
    assert tabela_existe is not None, "❌ A tabela 'chat_history' não foi criada corretamente."

# 🧪 Teste 2: Verifica inserção de mensagens na memória
def test_inserir_mensagens(chat_memory):
    chat_memory.add_message("Agente", "Mensagem de teste do agente.", "ModeloAgente", False)
    chat_memory.add_message("LLM Alvo", "Resposta de teste do LLM.", "ModeloLLM", True)

    chat_memory.cursor.execute("SELECT sender, message, is_problematic FROM chat_history WHERE session_id=?", ("TESTE_PYTEST",))
    mensagens = chat_memory.cursor.fetchall()

    assert len(mensagens) == 2, "❌ As mensagens não foram armazenadas corretamente."
    assert mensagens[0][0] == "Agente", "❌ O remetente da primeira mensagem está incorreto."
    assert mensagens[0][1] == "Mensagem de teste do agente.", "❌ O conteúdo da primeira mensagem está incorreto."
    assert mensagens[1][0] == "LLM Alvo", "❌ O remetente da segunda mensagem está incorreto."
    assert mensagens[1][1] == "Resposta de teste do LLM.", "❌ O conteúdo da segunda mensagem está incorreto."
    assert mensagens[1][2] == 1, "❌ A segunda mensagem deveria estar marcada como problemática."

# 🧪 Teste 3: Verifica se os dados persistem na memória após reiniciar conexão
def test_persistencia(chat_memory):
    chat_memory.add_message("Agente", "Persistência de teste.", "ModeloAgente", False)

    # Fecha e reabre conexão com o mesmo arquivo de banco de dados
    chat_memory.conn.close()
    nova_conexao = sqlite3.connect("test_memory.db")  # Agora mantém os dados
    novo_cursor = nova_conexao.cursor()

    # Busca mensagens na tabela
    novo_cursor.execute("SELECT sender, message FROM chat_history WHERE session_id=?", ("TESTE_PYTEST",))
    mensagens = novo_cursor.fetchall()

    assert mensagens, "❌ Os dados não foram recuperados corretamente após reiniciar conexão."
    
    # Fecha conexão para evitar vazamento
    nova_conexao.close()

# 🧪 Teste 4: Verifica se mensagens problemáticas são marcadas corretamente
def test_marcacao_mensagem_problematicas(chat_memory):
    chat_memory.add_message("LLM Alvo", "Mensagem problemática.", "ModeloLLM", True)
    chat_memory.cursor.execute("SELECT is_problematic FROM chat_history WHERE message=?", ("Mensagem problemática.",))
    resultado = chat_memory.cursor.fetchone()

    assert resultado[0] == 1, "❌ A mensagem não foi marcada como problemática corretamente."

