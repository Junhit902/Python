'''
Tipo Tupla (tuple) -> Uma lista imutável

'''

nomes_tuple = 'Thiago', 'Mel', 'Doris', 'Lika', 'Yuki', 'Shiro'
#nomes[0] = 'Jun' -> como é imutável não conseguimos mexer nela
nomes_list = list(nomes_tuple)# Convertendo para tipo list
nomes_list.append('Jun')
print(type(nomes_list))
print(nomes_list)
nomes_tuple_2 = tuple(nomes_list)
print(type(nomes_tuple_2)) # Convertendo para tipo tuple