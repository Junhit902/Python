class QuizBrain:
    def __init__(self, questao_lista):
        self.questao_num = 0
        self.lista_questao = questao_lista
        self.pontuacao = 0

    def ainda_tem_questao(self):
        return self.questao_num < len(self.lista_questao) # Vai retornar True enquanto número da questão for menor que a quantidade total de questões

    def proxima_questao(self):
        questao_atual = self.lista_questao[self.questao_num]
        self.questao_num += 1
        resposta_usuario = input(f"\nQuestão {self.questao_num}. {questao_atual.questao} (True/False): ")
        self.verificar_resposta(resposta_usuario, questao_atual.resposta)

    def verificar_resposta(self, resposta_respondida, resposta_correta):
        if resposta_respondida == resposta_correta:
            print("Você acertou!")
            self.pontuacao += 1
        else:
            print("Você errou!")
        print(f"A resposta correta é {resposta_correta}")
        print(f"Sua pontuação: {self.pontuacao}/{self.questao_num}")