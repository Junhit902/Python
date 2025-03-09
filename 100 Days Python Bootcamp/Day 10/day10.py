import os

def soma(n1, n2):
    soma = n1 + n2
    return soma

def subtracao(n1, n2):
    subtracao = n1 - n2
    return subtracao

def multiplicacao(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao

def divisao(n1,n2):
    divisao = n1 / n2
    return divisao

calculadora: dict[str,float]={
    "+": soma,
    "-": subtracao,
    "*": multiplicacao,
    "/": divisao
}

resetar = True

numero1 = float(input("Digite um número: "))

while resetar:
    numero2 = float(input("Digite um segundo número: "))

    print("\nEscolha uma dessas operações que deseja realizar:")
    for simbolo in calculadora:
        print(simbolo)

    operacao = input("\nDigite qual operacão deseja realizar: ")
    
    if operacao in calculadora:
        resultado = calculadora[operacao](numero1, numero2)
        print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")
    else:
        os.system("cls")
        print("Digite uma operação correta!\n")
        break

    continuar = input(f"\nVocê quer continuar a fazer mais uma operação com o resultado({resultado})? Digite (s)Sim ou (n)Não: ").lower()

    if continuar == "s":
        os.system("cls")
        numero1 = resultado
        print(f"Resultado anterior = {resultado}")
    elif continuar == "n":
        os.system("cls")
        print("Desligando...")
        resetar = False