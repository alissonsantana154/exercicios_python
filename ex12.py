# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$'))
desconto = 5

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de {desconto}% vai custar R${preco_final:.2f}')