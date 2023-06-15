# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
if num1 >= num2 and num1 >= num3 and num2 >= num3:
    print(f'Ordem decrescente dos valores: {num3}, {num2} e {num1}')
elif num2 >= num1 and num2 >= num3 and num1 >= num3:
    print(f'Ordem decrescente: {num3}, {num1} e {num2}.')
elif num3 >= num1 and num3 >= num2 and num2 >= num1:
    print(f'Ordem decrescente: {num1}, {num2} e {num3}.')
elif num1 >= num3 and num1 >= num2 and num3 >= num2:
    print(f'Ordem decrescente: {num2}, {num3} e {num1}')
elif num3 >= num1 and num3 >= num2 and num1 >= num2:
    print(f'Ordem decrescente: {num2}, {num1} e {num3}')
elif num2 >= num3 and num2 >= num1 and num3 >= num1:
    print(f'Ordem decrescente: {num1}, {num3} e {num2}')