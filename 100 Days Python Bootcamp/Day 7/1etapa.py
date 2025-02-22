import random

lista_palavras = ["Cachorro", "Carro", "Tartaruga", "Notebook", "Lapis", "Ventilador", "Internet", "Celular"]

palavra = random.choice(lista_palavras).upper()
palavra_escondida = "_" * len(palavra)
letras_corretas = []
vidas = 6

print(palavra)
print(palavra_escondida)

while vidas != 0:
    letra_usuario = input("Digite uma letra que possa conter na palavra misteriosa: ").upper()
    if letra_usuario not in palavra:
        vidas -= 1
        print(f"Você errou! Agora restam mais {vidas} vidas.")

    palavra_formando = ""

    for letra in palavra:
        if letra == letra_usuario:
            letra = letra_usuario
            letras_corretas.append(letra_usuario)
            palavra_formando += letra
        elif letra in letras_corretas:
            palavra_formando += letra
        else:
            letra = "_"
            palavra_formando += letra
    print(palavra_formando)
    
print("Voçê perdeu! Tente novamente.")