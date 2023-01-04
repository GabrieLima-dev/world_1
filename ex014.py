# Escreva um programa que converta uma temperatura digitada de graus celsius para Fahrenheit e Kelvin.

tc = float(input('Digite aqui a temperatura em graus celsius a ser convertida: '))

tf = (tc*1.8) + 32
tk = tc + 273.15

print('A temperatura {} °C corresponde a {} °F e a {} K'.format(tc, tf, tk))