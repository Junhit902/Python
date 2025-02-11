import random

list_palavra = ["computador", "janela", "guitarra", "oceano", "montanha", "livro", "relógio"]

palavra_escolhida = random.choice(list_palavra).upper()
print(palavra_escolhida)

letra_palavra = input("Adivinhe qual letra pode conter na palavra misteriosa: ").upper()


for letras in palavra_escolhida:
    if letra_palavra == letras:
        print("acertou a letra!")
    else:
        print("Não contém essa letra nessa palavra")
