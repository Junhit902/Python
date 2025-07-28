"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Thiago Jun'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.upper()) # Vai colocar tudo em maíusculo
print(string.zfill(100)) # Vai colocar zeros à esquerda para completar o número de caracteres que faltam