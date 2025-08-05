from dados import dados_paises
import ascart
import random
import os

perdeu = False
nova_pontuação = 0
pontuacao_total = nova_pontuação

def comparacao(pais1, pais2):
    pop1 = dados_paises[pais1]['populacao']
    pop2 = dados_paises[pais2]['populacao']
    if dados_paises[pais1]['pais'] != dados_paises[pais2]['pais']:
        if pop1 > pop2:
            return pais1
        else:
            return pais2

def resultado(opcao, pais_correta, pontos, pais1, pais2, pontuacao_final):
    if opcao == "A" and dados_paises[pais1]['pais'] == dados_paises[pais_correta]['pais']:
        print(f"\nParabéns! Você acertou o país com a maior população: {dados_paises[pais_correta]['pais']}.")
        pontos += 1
        return pontos
    elif opcao == "B" and pais2 == pais_correta:
        print(f"\nParabéns! Você acertou o país com a maior população: {dados_paises[pais_correta]['pais']}.")
        pontos += 1
        return pontos
    else:
        os.system("cls")
        print(f"\nVocê errou! Continue treinando. Total de pontos: {pontuacao_final}")
        return pontos
    
while perdeu is False:
    print(ascart.titulo)
    print("Qual é o país que possui a maior população?")
    pais_a = random.choice(range(0, len(dados_paises)))
    pais_b = random.choice(range(0, len(dados_paises)))
    print(f"\nPaís A: {dados_paises[pais_a]["pais"]} \nÁrea(km²): {dados_paises[pais_a]["area_km2"]} \nDescrição: {dados_paises[pais_a]["descricao"]}")
    print(ascart.vs)
    print(f"\nPaís B: {dados_paises[pais_b]["pais"]} \nÁrea(km²): {dados_paises[pais_b]["area_km2"]} \nDescrição: {dados_paises[pais_b]["descricao"]}")
    correta = comparacao(pais_a, pais_b)
    while True:
        escolha = input("\nDigite 'A' ou 'B' para o país com a maior população: ").upper()
        if escolha in ["A", "B"]:
            break
        else:
            print("Digite a opção correta, escolha entre as opções disponíveis 'A' ou 'B'!")
    pontuacao_total += resultado(escolha, correta, nova_pontuação, pais_a, pais_b, pontuacao_total)
    print(f"Pontuação total: {pontuacao_total}")
# Será escolhido dois países aleatoriamente para realizar a comparação
# Se o país for maior em população, ele vira outra letra. Ex.: A -> B
# O usuário tem que advinhar entre A ou B, digitando uma das opções
# Mas o mesmo país não pode repetir 3 vezes, ou seja, mesmo sendo maior em duas rodadas,
# na terceira rodada teria que ser o outro país que perdeu na 2 rodada no lugar
# O jogo continuará até o jogador perder e será contabilizado quantos pontos ele obteve