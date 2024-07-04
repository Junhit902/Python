import math

radius = input()

int_radius = int(radius)

volume = ((4.0/3) * round(math.pi, 5) * pow(int_radius,3))

print(f'VOLUME = {volume:.3f}') 