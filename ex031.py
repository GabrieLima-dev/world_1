# Desenvolva um programa que pergunte a distãncia de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

# mode 1
dist = float(input('Qual a distância da sua viagem em Quilômetros(KM)? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dist))

if dist <= 200:
    count = dist * 0.50
else:
    count = dist * 0.45
print('O preço da sua viagem é de R${:.2f}.'.format(count))

# mode 2
dist = float(input('''
Qual a distância da sua viagem em Quilômetros(KM)? '''))
print('Você está prestes a começar uma viagem de {}Km.'.format(dist))

price = dist * 0.50 if dist <= 200 else dist * 0.45

print('O preço da sua pássagem será de R${:.2f}.'.format(price))