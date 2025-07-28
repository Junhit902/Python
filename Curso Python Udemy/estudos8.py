nome = 'Thiago' # String
sobrenome = 'Honma' # String
idade = 21 # int
ano_nascimento = 2024 - idade # int 
maior_de_idade = idade >= 18 #Boolean
altura_metros = 1.85 # float

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros: ' +str(altura_metros)+ 'm') # Podemos concatenar(juntar) palavras e argumentos com o
# operador aritmetico (+), no caso do exemplo acima, a altura em metros foi convertida de float para String
# pois o python não consegue concatenar argumentos de tipos diferentes
