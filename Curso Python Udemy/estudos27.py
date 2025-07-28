'''

Introdução ao try/except

try -> tenta executar o código
expect -> ocorreu algum erro ao tentar executar

'''

numero_str = input('Digite um número para dobrar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro do número {numero_str} é {numero_float * 2:.2f}')
except:
    print(f'O que você digitou não é um número!')