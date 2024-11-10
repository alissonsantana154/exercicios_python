# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

valor = input('Digite algo: ')
print(f'O tipo primitivo desse valor é  {type(valor)}')
print(f'Só tem espaço? ', valor.isspace())
print(f'É um número? ', valor.isnumeric())
print(f'É alfanumérico? ', valor.isalpha())
print(f'Está em maiúsculas? ', valor.isupper())
print(f'Está em minúsculas? ', valor.islower())
print(f'Está capitalizado? ', valor.istitle())


