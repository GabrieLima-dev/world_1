# Crie um programa que leia o n ome completo de uma pessoa e mostre:
# O Nome com todas as letras mai´suculas e minúsculas.
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome.
name = str(input('Digite seu nome completo: '))

sp = name.strip()
name_ca = sp.upper()
name_lo = sp.lower()
lett_all = len(sp) - (sp.count(' '))  # contando os espaços
first_name = name.split()
lett_first = name.find(' ')

print('Analisando o seu nome...')
print("""Seu nome em maiúsculo é {}
Seu nome em minúsculo é {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras""".format(name_ca, name_lo, lett_all, first_name[0], lett_first))
