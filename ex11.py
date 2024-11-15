# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua á rea e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area_parede = largura * altura

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area_parede}m²')
quantidade_tinta = area_parede / 2
print(f'Para pintar essa paree, você precisará de {quantidade_tinta}l de tinta.')