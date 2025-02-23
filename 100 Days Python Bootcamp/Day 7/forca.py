import random
import os
import palavras

HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")


palavra = random.choice(palavras.lista_palavras).upper()
palavra_escondida = "_" * len(palavra)
letras_corretas = []
letras_repetidas = []
vidas = 7
game = True

print(palavra)

while game:
    os.system('cls')
    print(HANGMAN[vidas])
    print(f"{palavra_escondida}\n")
    print(f"Vidas restantes: {vidas}\n")
    letra_usuario = input("Digite uma letra que possa conter na palavra misteriosa: ").upper()

    while letra_usuario in letras_repetidas:
        os.system('cls')
        letra_usuario = input("Você já digitou essa letra! Digite uma letra que não tenha digitado: ")

    letras_repetidas.append(letra_usuario)

    if letra_usuario not in palavra:
        vidas -= 1
        print(f"Você errou! Agora restam mais {vidas} vidas.")
        os.system('cls')

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
    palavra_escondida = palavra_formando
    
    if "_" not in palavra_formando:
        game = False
        print("\nVocê venceu o jogo. Parabéns!")
    if vidas == 0:
        game = False
        print(f"\nA palavra era {palavra}")
        print("Você perdeu! Tente novamente.")