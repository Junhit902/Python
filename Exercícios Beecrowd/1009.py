name = input()
fixed = input()
solved = input()

float_fixed = float(fixed)
float_solved = float(solved)

bonus = (0.15 * float_solved)

total = (float_fixed + bonus)

print(f'TOTAL = R$ {total:.2f}')