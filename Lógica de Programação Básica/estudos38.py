''' Qual letra se repete mais vezes?'''

string = 'Thiago Jun Honma'.lower()
i = 0
letra_que_repete_mais_vezes_atual = ' '
letra_atual = ' '
qtd_que_se_repete_atual = 0
qtd_que_se_repete_anterior = 0

while i < len(string):
    letra = string[i]
    if letra == ' ':
        i += 1
        continue
    if letra_atual != letra:
        letra_atual = letra
        qtd_que_se_repete_atual = string.count(letra_atual)
        if qtd_que_se_repete_atual >= qtd_que_se_repete_anterior:
            qtd_que_se_repete_anterior = qtd_que_se_repete_atual
            letra_que_repete_mais_vezes_atual = letra_atual
    else: 
        i += 1
        continue
print(f'A letra "{letra_que_repete_mais_vezes_atual}" se repete mais vezes na frase, repetindo {qtd_que_se_repete_anterior}X.')