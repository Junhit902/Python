'''
Iterável -> str, range, etc. (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> me entrega o seu iterador
'''
# for letra in texto
texto = 'Thiago' #Iterável
iterador = iter(texto) # Mesma coisa que isso -> texto.__iter__() Iterador

while True:
    try:
        letra = next(iterador) # Mesma coisa que isso -> iterador.__next__()
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)