from turtle import Turtle, Screen
import random

tela = Screen()
corrida_continua = False

tela.setup(width=700, height=500)
aposta_usuario = tela.textinput(title="Corrida de Tartaruga", prompt="Faça a sua aposta, qual cor irá vencer?").lower()

cores = ["red",
    "blue",
    "green",
    "orange",
    "purple",
    "brown",
    "black",
    "yellow"]

cores_aleatorios = random.sample(cores, 8)
tartarugas = [] #lista para guardar tartarugas
pos_y = -100 # posição inicial

def linha_chegada():
    '''Função para desenhar a linha de chegada'''
    linha_chegada = Turtle()
    linha_chegada.penup()
    linha_chegada.goto(x=300, y=250)
    linha_chegada.setheading(270)
    linha_chegada.pendown()
    linha_chegada.pensize(10)
    linha_chegada.pencolor("red")
    linha_chegada.forward(500)

linha_chegada()

for cor_tartaruga in cores_aleatorios:
    tartaruga = Turtle(shape="turtle")
    tartaruga.color(cor_tartaruga)
    tartaruga.penup()
    tartaruga.goto(x=-300, y=pos_y)
    tartarugas.append(tartaruga)
    pos_y += 30

if aposta_usuario:
    corrida_continua = True

while corrida_continua:
    for tartaruga in tartarugas:
        distancia_aleatoria = random.randint(0, 10)
        tartaruga.forward(distancia_aleatoria)
    if tartaruga.xcor() > 290:
        cor_vencedor = tartaruga.pencolor().lower()
        corrida_continua = False
        if aposta_usuario == cor_vencedor:
            print(f"Você acertou! A cor vencedora foi {cor_vencedor}!")
        else:
            print(f"Você errou! A cor vencedora foi {cor_vencedor}!")


tela.exitonclick()