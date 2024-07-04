number = input()
hour = input()
amount = input()

int_number = int(number)
int_hour = int(hour)
float_amount = float(amount)

salary = (int_hour * float_amount)

print(f'NUMBER = {int_number}')
print(f'SALARY = U$ {salary:.2f}')