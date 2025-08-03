import random

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item += item 
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

'''No dia 13, aprendi como é importante usar o Debug nos códigos, onde você entende o processo e a lógica do código muito melhor, 
porque você vê passo a passo até chegar no resultado na qual é mostrado no console.'''