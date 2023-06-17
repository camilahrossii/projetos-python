# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
soma = pares =  impares = 0
for n in range(1,11):
    n = int(input(f'Informe o {n}º número: '))
    soma += n
    if n % 2 == 0:
        pares += 1
    elif n % 2 == 1:
        impares += 1
print(f'A soma dos valores informados é {soma}')
print(f'Quantidade números pares: {pares}')
print(f'Quantidade de números ímpares : {impares}')