import os

leilao: dict[str, float]={}
yes_no = True

while yes_no:
    nome = input("Qual é o seu nome?: ")
    lance = float(input("Quanto é o seu lance: R$"))

    leilao[nome] = lance

    continuar = input("Mais alguém para dar um lance? Digite 'S'(Sim) ou 'N'(Não): ").upper()

    if continuar == "S":
        yes_no = True
        os.system("cls")
    elif continuar == "N":
        yes_no = False
        os.system("cls")
        lance_maior = 0
        nome_maior = ""
        for nomes, lances in leilao.items():
            if lances > lance_maior:
                nome_maior = nomes
                lance_maior = lances
        print(f"O maior lance foi de {nome_maior} com o valor de R${lance_maior:.2f}")
    else:
        yes_no = True
        print("Digite corretamente!!!")
        os.system("cls")