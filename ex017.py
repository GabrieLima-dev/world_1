# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo,
# calcule e mostre o comprimento da hipotenusa.
# mode 1
import math
from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('COmprimento do cateto adjacente: '))
hyp = (co**2 + ca**2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hyp))

# mode 2
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('COmprimento do cateto adjacente: '))
hyp = sqrt(co**2 + ca**2)

print('A hipotenusa vai medir {:.2f}'.format(hyp))

# mode 3
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('COmprimento do cateto adjacente: '))
hyp = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hyp))
