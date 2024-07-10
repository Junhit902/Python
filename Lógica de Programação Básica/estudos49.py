'''
Introdução ao desempacotamento
'''

nomes = ['Thiago', 'Shiro', 'Mel', 'Lika', 'Doris', 'Yuki']
nome1, nome2, nome3, nome4, nome5, nome6 = nomes

print(nome1)


animes = ['Jujutsu Kaisen', 'Black Clover', 'Dragon Ball', 'Yuru Camp', 'Bocchi the Rock']
_, _, anime3,*resto = animes # _ -> variável que não vai ser usada e quando colocar * na frente da váriavel, mostra o resto

print(anime3, resto)