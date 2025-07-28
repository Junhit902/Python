'''

Flags (Bandeira) - Marcar um local 
None = não valor
is / is not  -> é / não é   (tipo, valor, identidade)
id = identidade

'''

# identidade(id)
valor = 'a'
valor2 = 'a'
valor3 = 'b'

print(id(valor))
print(id(valor2))
print(id(valor3)) # O id do valor 3 será diferente, pois o valor/literal passado é diferente

# None e is / is not
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo.')
else:
    print('Não faça nada.')

if passou_no_if is not None:
    print('Passou no if.')
else:
    print('Não passou no if.')