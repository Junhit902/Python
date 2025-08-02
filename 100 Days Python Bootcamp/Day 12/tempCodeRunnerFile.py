def is_prime(num):
    
    numero_div = [1, 2, 4]

    numero_div.insert(0, num)

    contador_primo = 0
    contador_nao_primo = 0

    for numero_primo in numero_div:
        if num % numero_primo == 0:
            contador_nao_primo += 1
        elif num % numero_primo != 0:
            contador_primo += 1

    if num == 1:
        print("False")
    elif contador_primo > contador_nao_primo or num == 2 or num == 3:
        print("True")
    else:
        print("False")
    
is_prime(73)
        