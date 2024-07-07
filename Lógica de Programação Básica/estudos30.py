"""
Exercício 1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

try: 
    int_numero = int(numero)
    if numero.isdigit():
        if int_numero % 2 == 0:
            print(f'O número {int_numero} é par.')
        elif int_numero % 2 == 1:
            print(f'O número {int_numero} é ímpar.')
except:
    print(f'O valor inserido não é um número inteiro!')

"""
Exercicio 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Que horas são agora? (apenas as horas em número inteiro): ')
try:
    int_horario = int(horario)

    if int_horario >= 0 and int_horario <= 11:
        print('Bom dia!')
    elif int_horario >= 12 and int_horario <= 17:
        print('Boa tarde!')
    elif int_horario >= 12 and int_horario <= 23:
        print('Boa noite!')
except:
    print('Você não digitou um número inteiro!')

"""
Exercicio 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite o seu primeiro nome: ')

try:
    if len(primeiro_nome) <= 4:
        print('Seu nome é curto!')
    elif len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
except:
    print('Você não digitou nada.')