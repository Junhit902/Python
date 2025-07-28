"""
Lista dentro de listas e seus índices
"""

escola = [
    #   0        1        2      3
    ['Pedro', 'Maria', 'João', 'Ana'], # Sala 1 -> 0
    
    #   0         1          2         3
    ['Paulo', 'Everson', 'Manoel', 'Bruna'], # Sala 2 -> 1
    #                                            0             1           2
    #   0         1          2         3                       4
    ['Rafael', 'Joana', 'Ricardo', 'Lucas'] # Sala 3 -> 2
]


print(escola)

#Se quiser dar um print na Bruna da Sala 2
print(escola[1][3])

# Se qiuser dar um print no Ricardo da Sala 3
print(escola[2][2])

# Se quise dar um print no professor 2 que está dentro de uma tupla que está dentro de uma 
# lista(Sala 3) que está dentro de uma outra lista(escola)
print(escola[2][4][1])

for sala in escola:
    print(sala)
    for aluno in sala:
        print(aluno)