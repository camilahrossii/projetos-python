# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n = int(input('Digite qualquer número (positivo ou negativo): '))
if n < 0:
    print(f'O número {n} é NEGATIVO!')
else:
    print(f'O número {n} é POSITIVO!')