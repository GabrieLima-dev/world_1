# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print(('-=')*13)
print('Analisador de Triângulos')
print(('-=')*13)
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a + b > c and b + c > a and a + c > b:
    print('''
    Os segmentos acima podem formar triângulo!''')
else:
    print('''
    Os segmentos acima não podem formar triângulo!''')
