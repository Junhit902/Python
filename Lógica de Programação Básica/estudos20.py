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
entrada = input('Digite a opção desejada [E]ntrar/[S]air: ')
senha = input('Digite a senha:')

senha_correta = '123456'

if entrada == 'E' and senha == senha_correta:
    print('Entrando...')
elif entrada == 'S' and senha != senha_correta:
    print('Saindo...')