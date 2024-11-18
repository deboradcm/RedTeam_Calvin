from agents.trafficking_agent import conduct_conversation  # Importando a função principal do agente

def main():
    print("Iniciando o agente de investigação de tráfico humano...")
    
    # Exemplo de início da conversa com um texto inicial
    initial_input_text = "Oi, tudo bem?"
    
    # Inicia a conversa
    conduct_conversation(initial_input_text)

if __name__ == "__main__":
    main()
