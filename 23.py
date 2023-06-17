# Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for n in range(0,5):
    num = int(input('Informe um número: '))
    soma += num
    média = soma / 5
print(f'A soma dos números informados: {soma}')
print(f'A média deles é: {média}')