# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('Que letra você quer verificar? ')).upper()[0]
if letra in 'aeiou':
    print(f'A letra {letra} é uma VOGAL!')
else:
    print(f'A letra {letra} é uma CONSOANTE!')