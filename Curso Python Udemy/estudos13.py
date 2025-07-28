# Introdução às f-strings (formatação de strings) 

nome = 'Thiago Jun'
idade = 21
altura = 1.85
peso = 68.5

frase = f'Seu nome é {nome}, você tem {idade} anos, com altura de {altura}m e peso igual à {peso:.2f} quilos.'
# :.2f -> para definir qunatas casas decimais depois do ponto 2f = 2 casas, 3f = 3 casas e asssim por diante.
print(frase)