# Um professor quer sortear  um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
first_st = input('Priumeiro aluno: ')
second_st = input('Priumeiro aluno: ')
third_st = input('Priumeiro aluno: ')
bedroom_st = input('Priumeiro aluno: ')
student = choice([first_st, second_st, third_st, bedroom_st])

print(' O aluno foi {}.'.format(student))
