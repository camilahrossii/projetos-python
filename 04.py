# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salário = float(input('Salário bruto por hora: R$'))
horas = float(input('Horas trabalhadas no mês: '))
bruto = salário * horas
ir = (bruto * 11) / 100
inss = (bruto * 8) / 100
sindicato = (bruto * 5) / 100
descontos = ir + inss + sindicato
liquido = bruto - descontos
print(f'+ Salário Bruto: R$ {bruto}')
print(f'- IR (11%): R${ir}')
print(f'- INSS (8%): R${inss}')
print(f'- Sindicato (5%): R${sindicato}')
print(f'= Salário Líquido: R$ {liquido}')
