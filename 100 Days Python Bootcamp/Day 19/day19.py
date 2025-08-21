from turtle import Turtle, Screen

tartaruga = Turtle()
tela = Screen()

def mover_frente():
    tartaruga.forward(10)

tela.listen()
tela.onkey(key='space', fun=mover_frente)
tela.exitonclick()
