# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Digite qualquer número inteiro '))
count = number % 2
if count == 0:
    print('O número {} é par.'.format(number))
else:
    print('O número {} é ímpar.'.format(number))
