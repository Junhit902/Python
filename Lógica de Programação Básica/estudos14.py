# Formatação de Strings com o método format

a = 'Thiago'
b = 'Jun'
c = 'Honma'
d = 1.2

# frase1 = 'a:{} b{} c{} d:{}'

# frase2 = 'a:{0} b:{1} c:{2} d:{3:.3f}' # Por índice, começa com 0

frase3 = 'a={nome1} b={nome2} c={nome3} d={nome4:.3f}' # Por parâmetro nomeado

formato = frase3.format(nome1 = a, nome2 = b, nome3 = c, nome4 = d)

print(formato)