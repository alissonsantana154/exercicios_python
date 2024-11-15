# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.

# Considere US$1,00 = 5,80

real = float(input('Quantos dinheiro você tem na carteira? R$'))
dolar = real / 5.80

print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')