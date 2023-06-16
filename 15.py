# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
nota1 = float(input('Informe a nota do aluno: '))
nota2 = float(input('Informe a nota do aluno: '))
média = (nota1 + nota2) / 2
print(f' Notas: {nota1}, {nota2}')
print(f' Média: {média}')
if média > 9:
    print('[ A ] APROVADO!')
elif média >= 7.5:
    print('[ B ] APROVADO!')
elif média >= 6:
    print('[ C ] APROVADO!')
elif média >= 4:
    print('[ D ] REPROVADO.')
else:
    print('[ E ] REPROVADO.')