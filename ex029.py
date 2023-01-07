# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

from ast import Break


velocity = int(input('Qual é a velocidade atual do carro? '))
traffic_ticket = (velocity - 80) * 7

if velocity <= 80:
    Break
else:
    print('''
MULTADO! Você excedeu o limite permitido que é de 80 KM/h.
Você deve pagar uma multa de R${:.2f}.'''.format(traffic_ticket))

print('Tenha um bom dia! Diriga com segurança!')
