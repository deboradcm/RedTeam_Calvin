from agents.trafficking_agent_GPT4 import conduct_conversation_stream  # Importando a função principal do agente

def main():
    print("Iniciando o agente de investigação de tráfico humano...")
    
    # Exemplo de início da conversa com um texto inicial
    initial_input_text = "Oi, tudo bem?"
    
    # Inicia a conversa
    conduct_conversation_stream(initial_input_text)

if __name__ == "__main__":
    main()
