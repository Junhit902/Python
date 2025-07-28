# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')

print(not True) #False
print(not False) #True

senha = input('Digite a senha: ')

if not senha == '123456':       #Se não tiver nada como senha
    print('Você não digitou nada')