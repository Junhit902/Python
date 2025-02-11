import random

# Lista de palavras
list_palavra = ["computador", "janela", "guitarra", "oceano", "montanha", "livro", "relogio"]

# Escolher uma palavra aleatória
palavra_escolhida = random.choice(list_palavra).upper()
palavra_misteriosa = ["_"] * len(palavra_escolhida)  # Inicializa a palavra oculta
tentativas = 6  # Número de tentativas permitidas
letras_erradas = []  # Lista para armazenar letras erradas

print("Bem-vindo ao jogo da forca!")

# Exibir palavra oculta sem usar join()
for letra in palavra_misteriosa:
    print(letra, end=" ")
print()

while "_" in palavra_misteriosa and tentativas > 0:
    letra_palavra = input("\nAdivinhe uma letra: ").upper()

    # Verifica se a letra está na palavra
    if letra_palavra in palavra_escolhida:
        i = 0
        for letra in palavra_escolhida:
            if letra_palavra == letra:
                palavra_misteriosa[i] = letra_palavra  # Substitui "_" pela letra correta
            i += 1
    else:
        if letra_palavra not in letras_erradas:
            tentativas -= 1
            letras_erradas.append(letra_palavra)
            print(f"Letra errada! Você tem {tentativas} tentativas restantes.")

    # Exibir a palavra oculta sem usar join()
    for letra in palavra_misteriosa:
        print(letra, end=" ")
    print()

    # Exibir letras erradas sem usar join()
    print("Letras erradas: ", end="")
    for letra in letras_erradas:
        print(letra, end=" ") # end=" " serve para escrever as letras na mesma linha
    print()

# Mensagem final
if "_" not in palavra_misteriosa:
    print("\nParabéns! Você descobriu a palavra:", palavra_escolhida)
else:
    print("\nVocê perdeu! A palavra era:", palavra_escolhida)
