import turtle as t
from turtle import Screen
import random

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

def desenhar_spirograph(angulo):
    for _ in range(int(360 / angulo)):
        tartaruga.pencolor(cores_aleatorias())
        tartaruga.circle(100)
        tartaruga.setheading(tartaruga.heading() + angulo)

desenhar_spirograph(5)    

tela.exitonclick()
