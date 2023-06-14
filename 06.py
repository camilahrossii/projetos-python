# Faça um Programa que peça dois números e imprima o maior deles.
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')))
print(f'Você digitou os valores {num}')
print(f'O maior é o {max(num)}')
print(f'O menor é o {min(num)}')