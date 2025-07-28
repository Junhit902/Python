import random

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
cartas_comp = []
cartas_jogador = []

contador = 2

def distribuir_cartas():
    for carta in range(contador):
        carta_c = random.choice(cartas)
        carta_j = random.choice(cartas)
        cartas_comp.append(carta_c)
        cartas_jogador.append(carta_j)

def pegar_mais_carta():
    carta_j = random.choice(cartas)
    cartas_jogador.append(carta_j)

distribuir_cartas()

print(f"{cartas_comp} = Computador")
print(f"{cartas_jogador} = Jogador")

ponto_comp = sum(cartas_comp)
ponto_jogador = sum(cartas_jogador)

print(f"Pontos do Computador = {ponto_comp}")
print(f"Pontos do jogador = {ponto_jogador}")


if ponto_jogador < 21:
    carta_mesa = input("[1]Pegar mais uma carta \n[2]Jogar na mesa \nEscolha umas dessas opções: ")
    if carta_mesa == "1":
        pegar_mais_carta()
        ponto_jogador = sum(cartas_jogador)
        print(f"Pontos do jogador = {ponto_jogador}")
    elif carta_mesa == "2":
        if ponto_jogador > ponto_comp:
            print("Você ganhou! Parabéns.")
        elif ponto_jogador < ponto_comp:
            print("Você perdeu!")
        elif ponto_jogador == ponto_comp:
            print("Empate!")
elif ponto_jogador == 21:
    print(ponto_comp)
    print(ponto_jogador)
    print("Você ganhou!")
else:
    print(ponto_comp)
    print(ponto_jogador)
    print("Você perdeu!")