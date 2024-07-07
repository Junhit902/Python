'''
Operadores de atribuição

=   +=  -=  *=  /=  //=  **=  %=

'''

condicao = True
contador = 0

# while condicao:
#     par_impar = input('Digite um numero inteiro qualquer: ')
#     int_par_impar = int(par_impar)
#     int_par_impar %= 2
#     if int_par_impar == 0:
#         print(f'O número {par_impar} digitado é par!')
#         contador +=1
#         print(f'Contador: {contador}')
#     else:
#         print(f'O número {par_impar} digitado é ímpar!')
#         contador +=1
#         print(f'Contador: {contador}')


while contador < 100:
    contador += 1
    if contador == 7:
        print('Não vou mostrar o %d.' %contador)
        continue
    if contador >= 20 and contador <= 30:
        print('Não vou mostrar o', contador)
        continue
    print(contador)

