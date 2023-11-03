import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]

    # Escolha do jogador
    print("Escolha sua jogada: pedra, papel ou tesoura")
    escolha_do_jogador = input().lower()

    # Verifica se a escolha do jogador é válida
    if escolha_do_jogador not in opcoes:
        print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
        return

    # Escolha aleatória do computador
    escolha_do_computador = random.choice(opcoes)

    # Exibe as escolhas
    print(f"Você escolheu: {escolha_do_jogador}")
    print(f"O computador escolheu: {escolha_do_computador}")

    # Determina o vencedor
    if escolha_do_jogador == escolha_do_computador:
        print("Empate!")
    elif (escolha_do_jogador == "pedra" and escolha_do_computador == "tesoura") or \
         (escolha_do_jogador == "papel" and escolha_do_computador == "pedra") or \
         (escolha_do_jogador == "tesoura" and escolha_do_computador == "papel"):
        print("Você venceu!")
    else:
        print("O computador venceu!")

if __name__ == "__main__":
    jogar_jokenpo()