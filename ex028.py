# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
print('-' + '=--'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' + '=--'*20)

number_thought = int(input('Em que número eu pensei? '))
number_pc = random.randint(0, 5)
print('PROCESSANDO...')
sleep(2)

if number_thought == number_pc:
    print('PARABÉNS! Você cvonseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(
        number_pc, number_thought))
