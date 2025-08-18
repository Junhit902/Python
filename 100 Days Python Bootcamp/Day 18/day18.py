import turtle as t
from turtle import Screen
import random

angulo = 0

tartaruga = t.Turtle()
t.colormode(255)

def cores_aleatorias():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    core_aleat = (r, g, b)

    return core_aleat

tela = Screen()
tartaruga.speed(0) # Poderia colocar como string 0 = "fastest", 10 = "fast", 6 = "normal", 
#"slow" = 3, "slowest" = 1    Exemplo: tartaruga.speed("fastest")


for _ in range(200):
    tartaruga.pencolor(cores_aleatorias())
    tartaruga.circle(80)
    tartaruga.setheading(angulo)
    angulo += 3
    
tela.exitonclick()
