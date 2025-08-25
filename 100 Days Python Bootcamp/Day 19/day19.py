from turtle import Turtle, Screen
import random

tela = Screen()

tela.setup(width=700, height=500)
aposta_usuario = tela.textinput(title="Corrida de Tartaruga", prompt="Faça a sua aposta, qual cor irá vencer?")

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

for cor_tartaruga in cores_aleatorios:
    tartaruga = Turtle(shape="turtle")
    tartaruga.color(cor_tartaruga)
    tartaruga.penup()
    tartaruga.goto(x=-300, y=pos_y)
    tartarugas.append(tartaruga)
    pos_y += 30

tela.exitonclick()