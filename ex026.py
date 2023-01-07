# Faça um programa que leia um frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

phrase = str(input('Digite uma frase: ')).strip().lower()


print(''' A letra A aparece {} vezes na frase.
A primeira letra A apareceu na posição {}.
A última letra A apareceu na posição {}.'''.format(phrase.count('a'), phrase.find('a') + 1, phrase.rfind('a') + 1))
