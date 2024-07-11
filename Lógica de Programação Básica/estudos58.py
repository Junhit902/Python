'''
Operação ternária -> condição de uma linha apenas
<valor> if <condição> else <outro valor>
'''

condicao = 10 == 10
print('Valor' if condicao else 'outro valor')


digito = '9'
cpf = ''
int_digito = int(digito)
cpf += digito if int_digito <= 9 else 0
print(cpf)


# Se as duas condições forem True vai exibir o Valor
# Se apenas a primeria condição for True vai exibir Valor
# Se apenas a segunda condição for True vai exbir Outro Valor
# Se as duas condições forem False vai exibir Nenhum dos valores
print('Valor' if False else 'Outro valor' if False else 'Nenhum dos valores')