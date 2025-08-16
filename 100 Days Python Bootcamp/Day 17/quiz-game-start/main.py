from question_model import Questao
from data import question_data
from quiz_brain import QuizBrain

banco_de_questoes = []

for questao in question_data:
    texto = questao["question"]
    resposta = questao["correct_answer"]
    nova_questao = Questao(texto, resposta)
    banco_de_questoes.append(nova_questao)

questao = QuizBrain(banco_de_questoes)

while questao.ainda_tem_questao():
    questao.proxima_questao()

print("\nMuito bem, você respondeu todas as questões!")
print(f"Sua pontuação final é {questao.pontuacao} de {len(questao.lista_questao)}")