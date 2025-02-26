letras_alfabeto = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def cipher(mensagem_original, numero_shift, direcao):
    mensagem_encryptado = ""
    if direcao == "decode":
            numero_shift *= -1
    for letra in mensagem_original:
        letra_encryptado = letras_alfabeto.index(letra) + numero_shift
        letra_encryptado %= len(letras_alfabeto)
        mensagem_encryptado += letras_alfabeto[letra_encryptado]
    print(f"A sua mensagem {direcao}d: {mensagem_encryptado}")

continuar = True

while continuar:

    opcao = input("Digite 'encode' para encryptar e 'decode' para decryptar: ").lower()
    mensagem = input("Digite a sua mensagem: ").lower()
    shift = int(input("Digite o número de shift: "))

    cipher(mensagem_original=mensagem, numero_shift=shift, direcao=opcao)

    seguir = input("Você deseja continuar digite 'sim' ou 'não': ")
    if seguir != 'sim':
        continuar = False