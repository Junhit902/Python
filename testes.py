def quadrado(x):
    return x ** 2

valores = [2, 4, 6]
resultado = list(map(quadrado, valores))
print(resultado)  # [4, 16, 36]
