'''
Interpolação Básica de Strings

s -string
i / d - inteiro
f - float
x / X - Hexadecimal (ABCDEF0123456789)
'''

nome = 'Thiago'
idade = 21
altura = 1.85

frase = '%s tem %d anos e %.2fm de altura' %(nome, idade, altura)

print(frase)

numero = 15

frase2 = 'O número %i em Hexadecimal é %08X' %(numero, numero)

print(frase2)