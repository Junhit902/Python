from turtle import Turtle, Screen
from cores import cores_variados
import random as r

angulos = [0, 90, 180, 270] # Modo standard 0 = leste, 90 = norte, 180 = oeste e 270 = sul

tartaruga = Turtle()
tela = Screen()
tartaruga.pensize(10)
tartaruga.speed(0) # Poderia colocar como string 0 = "fastest", 10 = "fast", 6 = "normal", 
#"slow" = 3, "slowest" = 1    Exemplo: tartaruga.speed("fastest")

for _ in range(300):
    tartaruga.pencolor(r.choice(cores_variados))
    tartaruga.forward(30)
    tartaruga.setheading(r.choice(angulos))
    
tela.exitonclick()
