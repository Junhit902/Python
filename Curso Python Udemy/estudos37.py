''' while e else'''

string = 'Thiago Jun'

i = 0 

while i < len(string):
    letra = string[i]

    if letra == ' ':
        print('Espaço encontrado.')
        break
    print(letra)
    i += 1
else:
    print('Espaço não encontrado.')

print('Fora do while.')