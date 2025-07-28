''' for'''

string = 'Thiago'
nova_string = ' '

for letra in string:
    print(letra)
    nova_string += f'*{letra}'

print(nova_string)