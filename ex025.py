# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Qual o seu nome completo? ')).strip().lower()

print('silva' in name)
