
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
num = float(input('Digite um número: '))

print('O número {} tem a parte inteira {:.0f}.'.format(num, num))

# from 2
# a partir da importação da função trunc com o módulo math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))
