primeiro_numero = input('Digite um número: ')
segundo_numero = input('Digite outro número: ')

int_primeiro = int(primeiro_numero)
int_segundo = int(segundo_numero)

if int_primeiro > int_segundo:
    print(f'O {primeiro_numero =} é maior que o {segundo_numero =}.')
elif int_segundo > int_primeiro:
    print(f'O {segundo_numero =} é maior que o {primeiro_numero =}.')
else:
    print('Os números são iguais.')