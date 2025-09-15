from turtle import Screen, Turtle

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor('Black')
tela.title("Jogo da cobrinha")

posicoes_iniciais = [(0, 0), (-20, 0), (-40, 0)] # Uma lista de tuplos com as posições dos quadrados

for posicao in posicoes_iniciais:
    quadrado = Turtle(shape="square")
    quadrado.color("white")
    quadrado.setpos(posicao)

tela.exitonclick()