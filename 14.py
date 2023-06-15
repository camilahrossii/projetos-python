# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('Em qual turno você estuda?')
print('[ M ] Matutino - [ V ] Vespertino - [ N ] Noturno')
turno = str(input('Digite aqui: ')).upper()[0]
if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
     print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')