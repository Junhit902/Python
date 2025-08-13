class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

usuario_1 = Usuario("Thiago", 22)
usuario_2 = Usuario("Jun", 22)

print(usuario_1.nome)
print(usuario_1.idade)
print(usuario_2.nome)
print(usuario_2.idade)