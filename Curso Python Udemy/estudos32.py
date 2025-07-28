'''

Repetição
while -> enquanto

Executa uma ação enquanto uma condição for verdadeira

Loop infinito -> Executa um código sem fim

'''

condicao = True
condicao2 = True

while condicao:
    nome = input('Digite um nome: ')
    print(f'Seu nome é {nome}.')
    opcao = input('Digite uma opção [1]Continuar ou [2]Sair: ')
    if opcao == '1':
        condicao = True
    elif opcao == '2':
        condicao = False
        print('Saindo...')
    else:
        print('Opção inválida.')
        condicao = True

while condicao2:
    print('Teste')
    break

print('Fora do while.')