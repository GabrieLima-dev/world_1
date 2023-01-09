# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# mode 1
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira mais um número: '))
list = [n1, n2, n3]

print('''
O menor número digitado foi {}.
O maior númeor digitado foi {}.'''.format(min(list), max(list)))

# mode 2
a = int(input('Insira um número: '))
b = int(input('Insira outro número: '))
c = int(input('Insira mais um número: '))

min = a
if b < a and b < c:
    min = b
if c < a and c < b:
    min = c

max = a
if b > a and b > c:
    max = b
if c > a and c > b:
    max = c

print('''
O menor número digitado foi {}.
O maior númeor digitado foi {}.'''.format(min, max))
