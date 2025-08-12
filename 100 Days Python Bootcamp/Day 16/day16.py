import prettytable

mesa = prettytable.PrettyTable()

mesa.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
mesa.add_column("Tipo", ["Elétrico", "Água", "Fogo"])
mesa.align = "l"

print(mesa)