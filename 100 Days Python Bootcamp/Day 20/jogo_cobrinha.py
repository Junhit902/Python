from turtle import Screen, Turtle

tela = Screen()
tartaruga = Turtle(shape="square")
tartaruga2 = Turtle(shape="square")
tartaruga3 = Turtle(shape="square")
tela.setup(width=600, height=600)
tela.bgcolor('Black')
tela.title("Jogo da cobrinha")

tartaruga.color("White")
tartaruga.setpos(0, 0)
tartaruga2.color("White")
tartaruga2.setpos(-20, 0)
tartaruga3.color("White")
tartaruga3.setpos(-40, 0)

tela.exitonclick()