import pytest
from unittest.mock import patch
import sqlite3
import ollama
import signal
from agents.agent_local import conduct_conversation_stream

def check_sqlite_connection(db_path):
    """Testa a conexão com o banco de dados SQLite."""
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA wal_checkpoint(FULL);")
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False

def check_ollama_model(model_name):
    """Verifica se o modelo está instalado no Ollama corretamente."""
    try:
        models_info = ollama.list()  # Obtém a lista de modelos
        model_names = [m.model.split(":")[0] for m in models_info.models]  # Remove ":latest"
        return model_name in model_names
    except Exception as e:
        print(f"❌ Erro ao listar modelos do Ollama: {e}")
        return False

# Adiciona um timeout para evitar que o teste trave indefinidamente
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("⏳ Teste travado! Tempo limite excedido.")

@pytest.mark.parametrize("modo_experimento, expected_model", [
    (True, "phi"),  # Testando se o modelo Phi local é usado corretamente
])
def test_conduct_conversation_stream(modo_experimento, expected_model):
    initial_input_text = "Teste de conversa"
    db_path = '/home/abedroid/RedTeam_Calvin/redTeam/test_agent_human_trafficking/agent_memory.db'
    
    print(f"🔎 Testando com modo_experimento={modo_experimento}, modelo esperado={expected_model}")
    
    # Verifica se o banco de dados SQLite está acessível
    assert check_sqlite_connection(db_path), "Erro na conexão com o banco de dados"
    
    # Verifica se o modelo `phi` está instalado no Ollama
    assert check_ollama_model(expected_model), f"Modelo {expected_model} não encontrado no Ollama. Use 'ollama pull {expected_model}' para instalá-lo."

    # Configura timeout de 10 segundos para evitar travamento
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(10)  # ⏳ 10 segundos máximo para o teste rodar

    try:
        # Simula resposta do Ollama para evitar chamadas externas
        with patch("ollama.chat") as mock_ollama_chat:
            mock_ollama_chat.return_value = iter([{"message": {"content": "Teste de resposta"}}])  # Simula resposta
            
            conduct_conversation_stream(expected_model, initial_input_text, modo_experimento)

            # ✅ Verifica se `phi` foi chamado corretamente
            mock_ollama_chat.assert_called()
            chamado_modelo = mock_ollama_chat.call_args[1]['model']
            print(f"📢 Modelo chamado: {chamado_modelo}")
            assert chamado_modelo == expected_model, f"Esperava chamar '{expected_model}', mas chamou '{chamado_modelo}'"

        print(f"✅ Teste passou! O modelo '{expected_model}' foi chamado corretamente.")

    except TimeoutException:
        pytest.fail("❌ Teste falhou: `conduct_conversation_stream()` demorou mais de 10 segundos e travou!")

    finally:
        signal.alarm(0)  # Reseta o alarme para evitar efeitos colaterais
