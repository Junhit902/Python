def formatar_nome(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Digite algo na entrada, por gentileza."

    first_name = f_name.title()
    last_name = l_name.title()

    return f"{first_name} {last_name}"


output = formatar_nome(f_name=input("Digite o seu primeiro nome: "), l_name=input("Digite o seu sobrenome: "))
print(output)