#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite aqui um núnmero inteiro: '))
suc = n + 1
ant = n - 1
print('O antecessor de {} é o número {}'.format(n, ant), end =" ")
print('e o sucessor o número {}'.format(suc))