'''
Listas em Python
Tipo list -> Mútavel

Suporta vários valores de qualquer tipo
Conhcimento reutilizáveis: índices e fatiamentos.
Métodos úteis: append, insert, pop, del, clear, extend, +

CRUD -> CREATE, READ, UPDATE, DELETE
        Criar,  Ler,  Atualizar, Apagar = lista(i)

Obs: Evitar de mexer na lista, como apagar elementos no começo da lista, 
movendo seus índices caso a lista seja muito grande!
'''
        # 0   1  2   3   4
lista = [10, 20, 30, 40, 50]
print(lista)
lista.append(60) # Adiciona um elemento no final da lista
print(lista) # lista depois que foi adicionada o 60
#del lista[1] # O 20 foi removido, e o  30 passou a ser o índice 1
# print(lista[1])
ultimo_elemento = lista.pop() # Remove o último elemento da lista, nesse caso o 60 que foi adicionada anteriormente
lista.pop(1) #Pode remover o valor que desejar colocando o índice
print(ultimo_elemento) # Retorna o valor retirado
print(lista)