# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
popA = 80000
popB = 200000
anos = 0
while popA < popB:
    calcA = ((popA * 3) / 100) 
    popA = calcA + popA
    calcB = ((popB * 1.5) / 100)
    popB = calcB + popB
    anos += 1
    print(f'No ano {anos} o crescimento foi de {calcA:.0f} para A e {calcB:.0f} para B.')
    print('-'*60)
print(f'\33[44mSão necessários {anos} para o país A ultrapasse ou iguale a população do país B.\33[m')