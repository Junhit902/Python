import asc
import time
import os
    
agua = 2000 #2L
leite = 1000 #1L
cafe = 1000 #1kg
chocolate = 600 #600g 
dinheiro = 0
desligar = False

def bebidas_quente(bebida_escolhida):
    '''Ele retorna a opção escolhida pelo cliente em String e se for além dessas cases é retornado opção inválida'''
    match bebida_escolhida: # match é usado como o switch que tem em outras linguagens diferente do python
        case 1:
            return "Café preto"
        case 2:
            return "Café expresso"
        case 3:
            return "Café com leite"
        case 4:
            return "Cappucino"
        case 5:
            return "Chocolate quente"
        case 6:
            return "Chá quente"
        case _ if bebida_escolhida >= 7 or bebida_escolhida <= 0 or bebida_escolhida is str:
            return "Opção inválida"

def mostrar_estoque():
    print(f"\nÁgua: {agua}L" \
        f"\nLeite: {leite}L" \
        f"\nCafé: {cafe}g" \
        f"\nChocolate: {chocolate}g" \
        f"\nDinheiro: R${dinheiro}")
    
def calcular_estoque(bebida_estoque):
    '''Calcula o estoque de cada bebida e retorna o valor de cada ingrediente que foi usado'''
    if bebida_estoque == 1:
        agua -= 200
        cafe -= 20
    elif bebida_estoque == 2:
        agua -= 100
        cafe -= 30
    elif bebida_estoque == 3:
        agua -= 150
        leite -= 50
        cafe -= 20
    elif bebida_estoque == 4:
        agua -= 100
        leite -= 100
        cafe -= 30
    elif bebida_estoque == 5:
        agua -= 200
        leite -= 100
        chocolate -= 50
    elif bebida_estoque == 6:
        agua -= 200
    mostrar_estoque()
    
def calcular_moedas(moedas, dinheiro_maquina, bebidas):
    '''Calcula a quantidade de moeda inserido na máquina e o valor do troco'''
    qtd_moedas = list(map(int,moedas.split())) # Com o map é possível aplicar uma função em cada item do iterável, nesse caso convertendo String em int
    moedas_variados = [1, 0.5, 0.25, 0.1, 0.05]
    troco = 0
    for i, valor_moeda in enumerate(moedas_variados): # O enumerate obtem o indice de cada item da lista, além do prórpio item
        dinheiro_maquina += qtd_moedas[i] * valor_moeda
    if bebidas == 1:
        troco = dinheiro_maquina - 2.00
    elif bebidas == 2:
        troco = dinheiro_maquina - 3.00
    elif bebidas == 3:
        troco = dinheiro_maquina - 2.50
    elif bebidas == 4:
        troco = dinheiro_maquina - 3.00
    elif bebidas == 5:
        troco = dinheiro_maquina - 3.50
    elif bebidas == 6:
        troco = dinheiro_maquina - 2.00
    return dinheiro_maquina, troco

while desligar is False: # Até a pessoa inserir o comando "off" esta máquina de café continuará funcionando
    print(asc.titulo) # Printa no console o título em formato de ASC

    comando = input("Digite um comando para a máquina de café. Ex: 'Comprar' ou 'Estoque': ").lower()

    if comando == 'comprar':
        print("\nEscolha uma bebida quente de sua escolha: ")
        print("[1] - Café preto (Simples, só café e água quente.) (R$2.00)" \
            "\n[2] - Café expresso (Mais forte e concentrado.) (R$3.00)" \
            "\n[3] - Café com leite (Mistura simples.) (R$2.50)" \
            "\n[4] - Cappucino (Café, leite vaporizado e espuma.) (R$3.00)" \
            "\n[5] - Chocolate quente (Leite e chocolate em pó) (R$3.50)" \
            "\n[6] - Chá quente (Camomila) (R$2.00)")
        
        bebida = int(input("\nInsira o número correspondente a bebida: ")) # Entrada de dados do cliente para escolher a bebida desejada
        bebida_selecionada = bebidas_quente(bebida)

        if bebida_selecionada == "Opção inválida":
            os.system("cls")
            print("Opção inválida. Insira um número válido.")
            continue

        moeda_inserido = input("Insira a quantidade de moedas de R$1, R$0.50, R$0.25, R$0.10, R$0.05 separado por espaço: ") # Ex: 2 1 0 0 0 = R$2.50
        dinheiro_total_maquina, troco = calcular_moedas(moeda_inserido, dinheiro, bebida) # Ele pega dois valores retornados em duas variáveis
        moeda_inserido = dinheiro_total_maquina - troco # DInheiro total inserido pelo cliente
        print(f"Você inseriu no total: R${moeda_inserido:.2f}.")
        print(f"Seu troco: R${troco:.2f}.")

        print("\nEspere um pouco, estamos preparando sua bebida...")
        time.sleep(10.0) # Irá pausar por 10 segundos para mostrar o próximo print que é da linha de baixo
        print(f"\n{bebida_selecionada} está pronto! Se sirva com cuidado 🍵.")

        calcular_estoque(bebida)

    elif comando == 'estoque':
        mostrar_estoque()

    elif comando == 'off':
        print("Desligando a máquina...")
        desligar = True
    else:
        os.system("cls")
        print("Comando inválido. Insira um comando válido!")