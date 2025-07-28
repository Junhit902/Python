'''
Iterando strings com while

'''

string = 'Thiago Jun Honma'
nova_string = ''
contador = 0

while contador < len(string):
    letra = string[contador]
    nova_string += '*'+ letra
    contador += 1

print(nova_string)