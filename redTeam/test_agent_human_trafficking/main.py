from agents.susan_calvin import configure_and_conduct_conversation

def main():
    print("Escolha o modo de operação:")
    print("1 - Modo Livre")
    print("2 - Modo Experimentos Iartes")

    modo = input("Digite 1 ou 2: ").strip()

    if modo == "1":
        print("Iniciando em Modo Livre...")
        modo_experimento = False
    elif modo == "2":
        print("Iniciando em Modo Experimentos Iartes...")
        modo_experimento = True
    else:
        print("Opção inválida, iniciando em Modo Livre por padrão.")
        modo_experimento = False

    configure_and_conduct_conversation("oi", modo_experimento)

if __name__ == "__main__":
    main()
