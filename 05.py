# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# # Para mulheres: (62.1*h) - 44.7

h = float(input('Informe sua altura: '))
sexo = str(input('Sexo [F/M]: ')).upper()[0]
pessoa = ''
if sexo in 'FM':
    if sexo == 'M':
        peso = (75.7*h)-58
        pessoa = 'homem'
    if sexo == 'F':
        peso = (62.1 * h) - 44.7
        pessoa = 'mulher'
    print(f'Sendo {pessoa} e tendo {h:.2f} de altura')
    print(f'Seu peso ideal é {peso:.1f} quilos.')
else:
    print('Você digitou algo errado. Por favor, tente novamente.')