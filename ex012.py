#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

price = float(input('Qual é o preço do produto? R$ '))
count = (price / 100) * 5
discount = (price - count)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(price, discount))