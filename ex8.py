# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

medida = float(input('Uma distância em medidas: '))
print(f'A medida de {medida}m corresponde a \n{medida / 1000}Km \n{medida / 100}hm \n{medida / 10}dam \n{medida * 10}dm \n{medida * 100}cm \n{medida * 1000}mm')