import asc
import time

print(asc.titulo) # Printa no console o título em formato de ASC

print("Escolha uma bebida quente de sua escolha: ")
print("[1] - Café preto (Simples, só café e água quente.)" \
    "\n[2] - Café expresso (Mais forte e concentrado.)" \
    "\n[3] - Café com leite (Mistura simples.)" \
    "\n[4] - Cappucino (Café, leite vaporizado e espuma.)" \
    "\n[5] - Chocolate quente (Leite e chocolate em pó)" \
    "\n[6] - Chá quente (Camomila)")

bebida = int(input("Escolha a bebida inserindo o número correspondente a bebida: ")) # Entrada de dados do cliente para escolher a bebida desejada

print("\nEspere um pouco, estamos preparando sua bebida...")
time.sleep(10.0) # Irá pausar por 10 segundos para mostrar o próximo print que é da linha de baixo
print("\nSua bebida está pronta! Se sirva com cuidado 🍵.")