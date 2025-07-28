# if /   elif    / else
# se / senão se / se não

maior_idade = input("Você é maior de idade? Digite 'sim' ou 'não': ")

if maior_idade == 'sim':
    print("Você pode tirar a sua CNH.")
elif maior_idade == 'não':
    print("Você não pode tirar a sua CNH ainda.")
else:
    print("Você não digitou nem 'sim' nem 'não'")


print('FORA DOS BLOCOS!')