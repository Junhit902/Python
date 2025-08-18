import turtle as t
from turtle import Screen
import random

angulos = [0, 90, 180, 270] # Modo standard 0 = leste, 90 = norte, 180 = oeste e 270 = sul

tartaruga = t.Turtle()
t.colormode(255)

def cores_aleatorias():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    core_aleat = (r, g, b)

    return core_aleat

tela = Screen()
tartaruga.pensize(10)
tartaruga.speed(10) # Poderia colocar como string 0 = "fastest", 10 = "fast", 6 = "normal", 
#"slow" = 3, "slowest" = 1    Exemplo: tartaruga.speed("fastest")


for _ in range(300):
    tartaruga.pencolor(cores_aleatorias())
    tartaruga.forward(30)
    tartaruga.setheading(random.choice(angulos))
    
tela.exitonclick()
