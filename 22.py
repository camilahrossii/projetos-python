# Faça um programa que leia 5 números e informe o maior número.
lista = []
for c in range(0,5):
    n = int(input('Informe um número: '))
    lista.append(n)
lista.sort()
print(f'Os valores informados foram: {lista}')
print(f'O maior deles é o {max(lista)}')