from turtle import Turtle, Screen

tartaruga = Turtle()
tela = Screen()

def mover_frente():
    tartaruga.forward(10)

def mover_atrás():
    tartaruga.backward(10)

def sentido_horario():
    tartaruga.right(10)

def sentido_anti_horario():
    tartaruga.left(10)

def limpar_tela():
    tartaruga.reset()

tela.onkeypress(fun=mover_frente, key='w')
tela.onkeypress(fun=mover_atrás, key='s')
tela.onkeypress(fun=sentido_horario, key='d')
tela.onkeypress(fun=sentido_anti_horario, key='a')
tela.onkeypress(fun=limpar_tela, key='c')
tela.listen()

tela.exitonclick()