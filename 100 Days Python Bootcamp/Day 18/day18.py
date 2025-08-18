from turtle import Turtle, Screen

tartaruga = Turtle()
tela = Screen()

tartaruga.shape("turtle")
tartaruga.color("green")

for i in range(4):
    tartaruga.forward(100)
    tartaruga.left(90)
    tartaruga.forward(100)



tela.exitonclick()