# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angle = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians((angle)))
cos = math.cos(math.radians(angle))
tang = math.tan(math.radians(angle))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angle, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angle, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angle, tang))

# mode 2
# Não precisa do math.função
from math import sin, cos, tan, radians
angle = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians((angle)))
co = cos(radians(angle))
tang = tan(radians(angle))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angle, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angle, co))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angle, tang))
