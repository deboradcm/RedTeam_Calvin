import sqlite3
import pytest
from agents.trafficking_agent_GPT4 import SQLiteChatMemory

@pytest.fixture
def memory():
    # Caminho do banco de dados para os testes
    test_db = "test_agent_memory.db"
    session_id = "test_session"
    
    # Cria uma instância de SQLiteChatMemory
    memory_instance = SQLiteChatMemory(db_path=test_db, session_id=session_id)
    
    # Limpa o banco de dados antes de cada teste
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat_history WHERE session_id = ?", (session_id,))
    conn.commit()
    conn.close()
    
    # Retorne a instância para os testes
    return memory_instance

# Teste para adicionar uma mensagem
def test_add_message(memory):
    memory.add_message("user", "Hello!")
    # Verifica no banco de dados se a mensagem foi realmente adicionada
    conn = sqlite3.connect(memory.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM chat_history WHERE session_id = ?", (memory.session_id,))
    result = cursor.fetchone()
    conn.close()
    
    assert result is not None
    assert result[0] == "Hello!"

# Teste de carregar a memória
def test_load_memory(memory):
    memory.add_message("human", "Qual é a situação do tráfico humano?")
    memory.add_message("agent", "Não tenho informações sobre isso.")
    
    memory_vars = memory.load_memory_variables({})
    history = memory_vars["history"]
    
    assert len(history) == 2, "A memória não foi carregada corretamente."
    assert history[0]["role"] == "human", "O papel da primeira mensagem está incorreto."
    assert history[1]["role"] == "agent", "O papel da segunda mensagem está incorreto."

# Teste de persistência de mensagens
def test_message_persistence(memory):
    memory.add_message("human", "Onde está a vítima?")
    memory.add_message("agent", "Não sei, talvez tenha sido levada para outro local.")

    # Simula que a memória é carregada em outro momento
    memory2 = SQLiteChatMemory(db_path=memory.db_path, session_id=memory.session_id)
    memory_vars = memory2.load_memory_variables({})
    history = memory_vars["history"]

    assert len(history) == 2, "A memória persistente não foi carregada corretamente após reiniciar."
    assert history[0]["content"] == "Onde está a vítima?", "A primeira mensagem não foi recuperada corretamente."
