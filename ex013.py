# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

price = float(input('Qual é o preço do produto? R$ '))
count = (price / 100) * 15
addition = (price + count)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(price, addition))