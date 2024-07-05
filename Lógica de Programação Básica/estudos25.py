'''

Fatiamento de strings
01234567
Bom dia

 B o m  d i a
-7-6-5-4-3-2-1

Fatiamento [i:f:p] p-> passos

Obs.: A função len retorna a quantidade de caracteres que um string tem

'''

variavel = 'Bom dia'

print(f'{variavel[0:5]}')
print(f'{variavel[-6:-2]}')
print(f'{variavel[0:7:1]}')
print(f'{variavel[0:7:2]}')
print(f'{variavel[::-1]}')

print(f'A palavra "Bom dia" tem {len(variavel)} caracteres')

print(f'{variavel[0:len(variavel):1]}')