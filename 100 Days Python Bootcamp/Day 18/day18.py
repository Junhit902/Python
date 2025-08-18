from turtle import Turtle, Screen
import random
import cores

tartaruga = Turtle()
tela = Screen()

tartaruga.shape("turtle")
tartaruga.color("green")

i = 3

while i != 10:
    tartaruga.pencolor(random.choice(cores.cores_variados))
    for _ in range(i):
        tartaruga.forward(100)
        tartaruga.right(360/i) # Ângulo
    i += 1

tela.exitonclick()