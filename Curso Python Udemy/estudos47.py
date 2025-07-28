'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''
lista1 = ['Thiago', 120, True, 50.4]
lista2 = lista1

lista1.insert(0, 'Hello World!')
print(lista2) # Vai ser alterado na lista2 também, pois ele está apontando no mesmo local da mémoria que a lista1 está apontando

print('-'*50)

lista_a = [120, 140, 150, 160]
lista_b = lista_a.copy()

lista_a.insert(0,'Adicionei na lista a')
print(lista_b) # Aqui não vai ser alterado
print(lista_a)