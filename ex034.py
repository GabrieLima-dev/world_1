# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para saláriossuperiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

wage = float(input('Qual o salário do funcionário? '))

if wage <= 1250:
    count = wage * 0.15
    result = count + wage
else:
    count = wage * 0.10
    result = count + wage

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(wage, result))