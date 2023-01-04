# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta, pinta uma área de 2 metros cúbicos.

wid = float(input('Digite a largura da sua parede: '))
heig = float(input('Digite a altura da sua parede: '))
area = wid * heig
area_paint = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2.'.format(wid, heig, area))
print('Para pintar a sua parede, você precisará de {}l de tinta.'.format(area_paint))