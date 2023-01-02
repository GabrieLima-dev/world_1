#Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
dou = n * 2
tri = n * 3
sou = n ** (1/2)
print('O dobro de {} vale {}'.format(n, dou))
print('O triplo de {} vale {}'.format(n, tri))
print('A raiz quadrada de {} vale {:.2f}'.format(n, sou))