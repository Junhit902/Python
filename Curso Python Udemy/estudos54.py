"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
primeira_frase = '      A vida é feita de escolhas , faça as suas com sabedoria.         '
segunda_frase = primeira_frase.split(',')

terceira_frase = []

for i, primeira_frase in enumerate(segunda_frase):
    terceira_frase.append(segunda_frase[i].strip())

print(terceira_frase)
frases_unidas = ', '.join(terceira_frase)
print(frases_unidas)