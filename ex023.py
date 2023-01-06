# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

n = int(input('Informe um número: '))
unity = n // 1 % 10
ten = n // 10 % 10
hund = n // 100 % 10
thou = n // 1000 % 10

print("""Analisando o número {}
Unidade: {}
Dezena: {}
Centena {}
Milhar: {}""".format(n, unity, ten, hund, thou))
