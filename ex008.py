# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = int(input('Digite aqui um número em metros a ser convertido.'))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print('A medida de {:.1f}m corresponde a\n {} Km\n {} hm\n {} dam\n {} dm\n {} cm\n {} mm'.format(n , km, hm, dam, dm, cm, mm))