'''
for in com listas
Exercício
Exiba os índices da lista
'''

lista = ['Thiago', 879, True, 1.2]
lista.append('Jun')
lista.insert(2, 'Adicionei no índice 2.')
indice = range(len(lista))
for indices in indice:
    print('índice:',indices, lista[indices], type(lista[indices]))