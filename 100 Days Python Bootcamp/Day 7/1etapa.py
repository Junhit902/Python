import random

lista_palavras = ["guitarra", "carro", "notebook", "casa", "oceano", "casamento", "palavra", "livro", "lampada"]

palavra_aleatoria = random.choice(lista_palavras).upper()
palavra_misteriosa = "_" * len(palavra_aleatoria)
palavra_adivinhar = ""
vidas = 6
letras_corretas = []

print(palavra_aleatoria)
print(palavra_misteriosa)

while vidas > 0:
    letra_adivinhar = input("\nDigite a letra que possa conter na palavra: ").upper()
    if letra_adivinhar in palavra_aleatoria:
        for letra in palavra_aleatoria:
            if letra_adivinhar == letra:
                letra = letra_adivinhar
                letras_corretas.append(letra)
            else:
                letra = "_"
            palavra_adivinhar += letra
        print(f"Você tem {vidas} vidas faltando.")
    else:
        vidas -= 1
        print("Você errou a letra!")
        print(f"Você tem mais {vidas} vidas.")
    if "_" not in palavra_adivinhar:
        print("Você ganhou o jogo! Parabéns!")
    print(palavra_adivinhar)
    palavra_adivinhar = ""

print("Você perdeu, tente novamente.")