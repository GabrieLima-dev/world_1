# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ 1,00 = R$3,27

my_money = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = 3.27
end = my_money / dolar
print('Com R${:.2f} você pode comprar US${:.2f}'.format(my_money, end))