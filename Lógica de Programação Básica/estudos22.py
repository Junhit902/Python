# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# T h i a g o
#-6-5-4-3-2-1

nome = 'Thiago'

print(nome[2])
print(nome[-4])

print('a' in nome) # 'a' está em nome
print('z' in nome) # 'z' está em nome

print('g' not in nome) # 'g' não está em nome
print('z' not in nome) # 'z' não está em nome

nome2 = input('Digite um nome: ')
encontrar = input('Escolha uma letra ou mais que esteja no nome que digitou: ')

if encontrar in nome2:
    print(f'A(s) letra(s) {encontrar} está em {nome2}')
else:
    print(f'A(s) letra(s) {encontrar} não está em {nome2}')