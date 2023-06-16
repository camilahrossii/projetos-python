# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
anos = 0
while True:
    popA = float(input('Informe a popualção A: '))
    taxaA = float(input('Informe a taxa de crescimento: '))
    popB = float(input('Informe a populção B: '))
    taxaB = float(input('Informe a taxa de crescimento: '))    
    while popA < popB:
        calcA = ((popA * taxaA) / 100) + popA
        calcB = ((popA * taxaB) / 100) + popB
        popA = calcA
        popB = calcB
        anos += 1
        print(f'No ano {anos} a população de A foi para {popA:.0f} e a de B {popB:.0f}')
        print('-'*60)
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break