import math

a, b, c = input().split()

float_a = float(a)
float_b = float(b)
float_c = float(c)

triangule = (float_a * float_c)/2

circle = round(math.pi, 5) * pow(float_c,2)

trapezium = ((float_a + float_b) * float_c)/2

square = pow(float_b,2)

rectangule = float_a * float_b

print(f'TRIANGULO: {triangule:.3f}')
print(f'CIRCULO: {circle:.3f}')
print(f'TRAPEZIO: {trapezium:.3f}')
print(f'QUADRADO: {square:.3f}')
print(f'RETANGULO: {rectangule:.3f}')