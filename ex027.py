# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite seu nome completo: ')).title()
name_div = name.split()
last_name = len(name_div)

print('Muito prazer te conhecer!')
print('''
Seu primeiro nome é {}.
Seu último nome é {}.'''.format(name_div[0], name_div[last_name - 1]))
