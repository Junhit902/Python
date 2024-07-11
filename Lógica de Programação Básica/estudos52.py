'''
Faça uma lista de comprar com listas
O usuário deve ter a possiblidade de
inserir, apagar e listar valores da sua lista
Não permita que o pograma quebre com 
erros de índices inexistentes na lista
'''

import os

produtos = []

while True:
    print('\n\t---- Lista de Compras ----')
    print('1 - Inserir produtos')
    print('2 - Apagar produtos')
    print('3 - Listar produtos')
    print('4 - Sair')
    opcao = input('\nSelecione uma das opções: ')

    if opcao not in ['1','2','3','4']:
        os.system('cls')
        print('Opção inválida')
        continue

    if opcao == '1':
        produto = input('Digite o nome do produto:')
        produtos.append(produto)
        os.system('cls')
        print('Produto adicionado com sucesso!')
    elif opcao == '2':
        try:
            apagar = input('Digite o índice do produto que deseja apagar: ')
            int_apagar = int(apagar)
            apagado = produtos.pop(int_apagar)
            os.system('cls')
            print(f'Produto {apagado} apagado com sucesso!')
        except ValueError:
            os.system('cls')
            print('Erro! Digite um número para o índice que deseja apagar.')
        except IndexError:
            os.system('cls')
            print('Erro! O índice digitado não existe na lista.')
        except:
            os.system('cls')
            print('Erro desconhecido!')
    elif opcao == '3':
        os.system('cls')
        print('\n\t---- Lista de produtos ----')
        if produtos == []:
            print('Lista vazia!')
            continue
        for indice, prod in enumerate(produtos):
            print(f'{indice} - {prod}')
    elif opcao == '4':
        print('Obrigado por usar o programa!')
        break