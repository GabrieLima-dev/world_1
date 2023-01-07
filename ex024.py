# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
city = str(input('Em que cidade você nasceu? ')).strip().lower()

print(city.startswith('santo'))

# mode 2
nome = input('Em que cidade voê nasceu? ')
nome.strip()
print(nome[0:6].lower() == 'santo ')

# mode 3
cid = str(input('Em que cidade voê nasceu? ')).strip()

print(cid[:5].upper() == 'SANTO')
