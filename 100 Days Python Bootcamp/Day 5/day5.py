import random

letras = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

simbolos = [
    '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', 
    '', '^', '~', '`'
]

print("Bem vindo ao gerador de senhas!")
qtd_letra = int(input("Qual a quantidade de letra que você deseja que tenha na senha?: "))
qtd_numero = int(input("Qual a quantidade de números que você deseja que tenha na sua senha?: "))
qtd_simbolo = int(input("Qual a quantidade de símbolos que você deseja que tenha sua senha?: "))

i = 0
letra_senha = ""

for letras_escolhidas in letras:      
    if i < qtd_letra:
        i += 1
        letra = random.randrange(0, len(letras))
        letra_senha += letras[letra]
    else:
        break

j = 0
numero_senha = ""

for numeros_escolhidos in numeros:
    if j < qtd_numero:
        j += 1
        numero = random.randrange(0, len(numeros))
        numero_senha += numeros[numero]
    else:
        break

z = 0
simbolo_senha = ""

for simbolos_escolhidos in simbolos:
    if z < qtd_simbolo:
        z += 1
        simbolo = random.randrange(0, len(simbolos))
        simbolo_senha += simbolos[simbolo]
    else:
        break

senha_final = list(letra_senha + numero_senha + simbolo_senha) # Convertendo de String para lista
random.shuffle(senha_final) # Emabralha os elementos da lista

t = 0
senha_definitiva = ""

for senha_elemento in senha_final:
    t += 1
    if t < len(senha_final)+1:
        senha_definitiva += senha_elemento
    else:
        break

print(f"Uma senha aleatória foi gerada: {senha_definitiva}")