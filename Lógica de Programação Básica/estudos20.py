''' 
Operadores Lógicos 

and(e)  or(ou)  not(não)  

and -> Todas as condições tem que ser verdadeira
or -> Uma das condições tem que ser verdadeira
not -> Inverte o valor da condição

Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
São considerados falsy
(0) (0.0) ('') (False)
Também existe o tipo None que é
usado para representar um não valor

'''

# Exemplo de uso do operador and (e)
print('and (e)' + str(35 * '-'))
entrada = input('Digite a opção desejada [E]ntrar/[S]air: ')
senha = input('Digite a senha:')

senha_correta = '123456'

if entrada == 'E' and senha == senha_correta:
    print('Entrando...')
elif entrada == 'S' and senha != senha_correta:
    print('Saindo...')

# Exemplo de uso do operador or (ou)
print('or (ou)' + str(35 * '-'))
entrada2 = input('Digite a opção desejada [E]ntrar/[S]air: ')
if (entrada2 == 'E' or entrada2 == 'e'):
    senha2 = input('Digite a senha: ')
    senha2_correta = '123456'
    if senha2 == senha2_correta:
        print('Entrando...')
    elif senha2 != senha2_correta:
        print('Senha incorreta! Tente novamente')
else:
    print('Saindo...')


# Avaliação de curto circuito
print(35 * '-')
print(True and False and True)
print(True and 0 and True)
senha1 = input("Senha: ") or 'Sem senha'
print(senha1)