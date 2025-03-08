def is_leap_year(year):
    if year % 4 == 0:
        print("Leap")
        if year % 100 == 0:
            print("Not Leap")
            if year % 400 != 0:
                print("Not Leap")
                return False
            else:
                print("Leap")
                return True
    else:
        print("Not Leap")
        return False

output = is_leap_year(year=int(input("Digite um ano qualquer: ")))
print(output)