from turtle import Turtle, Screen

tartaruga = Turtle()
tela = Screen()

tartaruga.shape("turtle")
tartaruga.color("green")
tartaruga.forward(200)
tartaruga.right(90) # Indica o ângulo a tartaruga muda a direção
tartaruga.forward(200)


tela.exitonclick()