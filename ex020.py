# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
student_1 = input('Primeiro aluno: ')
student_2 = input('Segundo aluno: ')
student_3 = input('Terceiro aluno: ')
student_4 = input('Quarto aluno: ')
order = [student_1, student_2, student_3, student_4]
x = random.sample(order, k=len(order))

print('A ordem de apresentação será: {}'.format(x))
