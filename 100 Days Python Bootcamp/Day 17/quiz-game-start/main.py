from question_model import Questao
from data import question_data

banco_de_questoes = []

for questao in question_data:
    texto = questao["text"]
    resposta = questao["answer"]
    nova_questao = Questao(texto, resposta)
    banco_de_questoes.append(nova_questao)

print(banco_de_questoes[1].questao)