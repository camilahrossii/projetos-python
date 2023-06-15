# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produtos = (float(input('Informe o preço do produto 1: R$')),
            float(input('Informe o preço do produto 2: R$')),
            float(input('Informe o preço do produto 3: R$')))
menor = min(produtos)
if menor == produtos[0]:
    print(f'Você deveria comprar o produto 1 que custa R${menor:.2f}')
elif menor == produtos[1]:
    print(f'Você deveria comprar o produto 2 que custa R${menor:.2f}')
else:
    print(f'Você deveria comprar o produto 3 que custa R${menor:.2f}')
