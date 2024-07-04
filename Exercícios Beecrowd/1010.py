code1, units1, price1 = input().split()
code2, units2, price2 = input().split()

int_code1 = int(code1)
int_units1 = int(units1)
float_price1 = float(price1)

int_code2 = int(code2)
int_units2 = int(units2)
float_price2 = float(price2)

total = ((int_units1 * float_price1) + (int_units2 * float_price2))

print(f'VALOR A PAGAR: R$ {total:.2f}')