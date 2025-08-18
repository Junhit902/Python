from turtle import Turtle, Screen

tartaruga = Turtle()
tela = Screen()

tartaruga.shape("turtle")
tartaruga.color("green")

for _ in range(50):
    tartaruga.forward(10)
    tartaruga.penup()
    tartaruga.forward(10)
    tartaruga.pendown()


tela.exitonclick()