#Desenvolva um programa que leia as duas notas de um aluno, cacule e mostre a sua média.
note1 = float(input('Digite aqui a primeira nota '))
note2 = float(input('Digite aqui a segunda nota '))

average = (note1 + note2) / 2

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(note1, note2, average))