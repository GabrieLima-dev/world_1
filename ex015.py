# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pecorridos pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

mileage = float(input('Quantos km rodado? '))
days = float(input('Quantos dias alugado? '))

total = (mileage*0.15) + (days*60)
print('O total a pagar é de {:.2f}'.format(total))