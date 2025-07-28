'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

'''
lista = [10, 20, 30, 40, 50, 60, 70]

#append
lista.append(80)
print('append:',lista)

#insert
lista.insert(0, 90) # .insert(índice que você que colocar, valor que quer colocar)
print('insert:',lista)

#pop
lista.pop() #Remove o último elemento da lista e retorna o valor removido
elemento_removido = lista.pop(1) # Pode passar o índice do elemento que deseja remover
print('pop:',lista)
print(f'Elemento removido com pop: {elemento_removido}')

#del
del lista[2]
print('del:', lista)

#extend
lista2 = [100, 200, 300]
lista.extend(lista2) # Adiciona os elementos de uma lista a outra
print('extend:',lista)

# + (concatenação)
lista3 = lista + lista2
print('Concatenação (+):',lista3)

#clear
lista3.clear()
print(lista3)