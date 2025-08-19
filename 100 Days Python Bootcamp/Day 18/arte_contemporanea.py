import turtle
import random

lista_cores_rgb = [(139, 80, 53), (185, 163, 125), (138, 166, 176), (60, 111, 134), (17, 42, 73), (139, 62, 88), (162, 153, 44), (66, 119, 101), (147, 182, 171), (215, 210, 107), (76, 34, 29)]

tartaruga = turtle.Turtle()
repeticao = 0
posicao_x = -250
posicao_y = -200

turtle.colormode(255)
tartaruga.penup()
tartaruga.setposition(-250, -200)


while repeticao != 10:
    for _ in range(10):
        tartaruga.dot(30, random.choice(lista_cores_rgb))
        tartaruga.forward(50)
        tartaruga.penup()
    repeticao += 1
    posicao_y += 50
    tartaruga.setposition(posicao_x, posicao_y)
    
turtle.exitonclick()