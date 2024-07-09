'''Calculadora com while'''

condicao = True

while condicao:
    print('---------- CALCULADORA ----------')
    numero1 = input('Digite um número: ')
    numero2 = input('Digite um outro número: ')
    float_numero1 = 0
    float_numero2 = 0
    try: 
        float_numero1 = float(numero1)
        float_numero2 = float(numero2)
        print('Números recebidos!')
    except:
        print('Digite um número inteiro ou float!')
        continue
    operacao = input('Escolha uma operacao [1]Soma [2]Subtração [3]Multiplicação [4]Divisão: ')
    if operacao == '1':
        resultado = float_numero1 + float_numero2
        print(f'{float_numero1} + {float_numero2} = {resultado:.2f}')
    elif operacao == '2':
        resultado = float_numero1 - float_numero2
        print(f'{float_numero1} - {float_numero2} = {resultado:.2f}')
    elif operacao == '3':
        resultado = float_numero1 * float_numero2
        print(f'{float_numero1} x {float_numero2} = {resultado:.2f}')
    elif operacao == '4':
        if float_numero1 != 0 and float_numero2 != 0:
            resultado = float_numero1 / float_numero2
            print(f'{float_numero1} / {float_numero2} = {resultado:.2f}')
        else:
            print('Erro! Divisão por zero não é permitida!')
            continue
    else:
        print('Operação inválida! Retornando ao menu...')
        continue
    opcao = input('Quer continuar? [S]im ou [N]ão: ').lower().startswith('s' or 'n')
    if opcao:
        print('Voltando ao menu...')
        continue
    else:
        print('Saindo...')
        break
        
