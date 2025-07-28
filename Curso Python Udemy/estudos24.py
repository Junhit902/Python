"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 

"""

variavel = 'Thiago'

print(f'{variavel}')
print(f'{variavel:>15}')
print(f'{variavel:<15}')
print(f'{variavel:^15}')
print(f'{150.230940870:.2f}')
print(f'{15:08X}')
print(f'{-13000:-.2f}')
print(f'{12000:0=+10,.2f}')
print(f'{variavel!r}')