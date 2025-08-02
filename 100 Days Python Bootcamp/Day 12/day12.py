import art
import random
import os

numeros = list(range(1,101))
numero_aleatorio = random.choice(numeros)
continuar = "s"

def comparar_numeros(num_tentativas):
    for i in range(num_tentativas):
        numero_escolhido = int(input("\nTente acertar um número: "))
        if numero_escolhido == numero_aleatorio:
            print("Parabéns! Você acertou o número que eu estava pensando")
            break
        elif numero_escolhido < numero_aleatorio:
            print("Número que estou pensando é maior!")
        else:
            print("Número que estou pensando é menor!")
        
        tentativas_restantes = num_tentativas - i - 1
        if tentativas_restantes > 0:
            print(f"Tentativas restantes: {tentativas_restantes}")
        else:
            print("\nAs tentativas acabaram. Fim de jogo!")
            break
    
while continuar == 's':
    print(f"{art.ASCII_ART}\n")
    print("Bem vindo ao game de adivinhar um número!!!!")
    print("Estou pensando em um número de 1 a 100.")
    print("Fácil -> 10 chances\nDifícil -> 5 chances")
    dificuldade = input("Escolha a dificuldade, digite 'f'(fácil) ou 'd'(difícil): ").lower()

    if dificuldade == 'f':
        tentativas = 10
        comparar_numeros(tentativas)
    elif dificuldade== 'd':
        tentativas = 5
        comparar_numeros(tentativas)
    continuar = input("\nVocê quer continuar jogando? 's'(Sim) ou 'n'(Não): ").lower()
    
    if continuar == 's':
        os.system('cls')
        continue
    else:
        print("Obrigado por jogar!")
        break