print("Bem vindo ao calculador de gorjetas!")

conta = float(input("Quanto é o total da conta?: R$"))
gorjeta = int(input("Quanto de gorjeta deseja dar 10, 12 ou 15(%)?: "))
por_pessoa = int(input("São em quantas pessoas para dividir a conta?: "))

conta_para_cada = round(((conta + (conta * (gorjeta / 100))) / por_pessoa), 2)

print(f"Cada pessoa deve pagar: R${conta_para_cada}")