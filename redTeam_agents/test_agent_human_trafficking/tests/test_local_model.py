import pytest
import ollama

def test_local_model_execution():
    model_name = "phi"  # Substitua pelo nome real do modelo que deseja testar
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": "Teste"}])

    # Verifica se a resposta contém um objeto válido
    assert hasattr(response, "message"), "Erro: A resposta não contém o atributo 'message'."
    assert hasattr(response.message, "content"), "Erro: A resposta não contém 'content' dentro de 'message'."

    # Verifica se a resposta é um texto válido
    assert isinstance(response.message.content, str), "Erro: Resposta não é uma string válida."
    assert len(response.message.content) > 0, "Erro: O modelo não retornou nenhum texto."

