# Faça um Programa que leia três números e mostre o maior deles.
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O maior valor é o {max(num)}')
print(f'O menor valor é o {min(num)}')