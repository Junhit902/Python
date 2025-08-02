import random

numero_aleatorio = random.randint(1, 100)

def comparar_numeros(num_tentativas):
    for i in range(num_tentativas):
        numero_escolhido = int(input("Tente acertar um número: "))  # Convertendo para int
        
        if numero_escolhido == numero_aleatorio:
            print("Parabéns! Você acertou o número que eu estava pensando")
            break  # Sai do loop se acertar
        elif numero_escolhido < numero_aleatorio:
            print("Número que estou pensando é maior!")
        else:  # Se não é igual e não é menor, é maior
            print("Número que estou pensando é menor!")
        
        # Mostrar tentativas restantes
        tentativas_restantes = num_tentativas - i - 1
        if tentativas_restantes > 0:
            print(f"Tentativas restantes: {tentativas_restantes}")
    
    # Se saiu do loop sem acertar
    else:
        print(f"Acabaram as tentativas! O número era {numero_aleatorio}")

# Chamar a função
print(numero_aleatorio)
comparar_numeros(5)