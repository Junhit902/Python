'''
Listas em Python
Tipo list -> Mútavel

Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis: índices e fatiamentos
Métodos úteis: append, insert, pop, del, clear, extend, +
'''

string = 'Thiago' # 6 caracteres
print(len(string))
lista = []
print(type(lista))
    
    #    0      1      2        3
    #   -4     -3     -2       -1
lista1 = [123, 1.2, 'Thiago', True]
print(lista1)
print(lista1[0], lista1[-4])
print(type(lista1[-2]))
print(lista1[-2].upper())