# Faça um Programa que pergunte quanto você ganha por hora e o 
# número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

salário = int(input('Qual o salário por hora? R$'))
horas = int(input('Quantas horas trabalhados por mês? '))
total = salário * horas
print(f'Seu salário por hora é {salário} e você trabalhar {horas} por mês.')
print(f'Sendo assim, seu salário é de R${total}')