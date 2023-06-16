# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Nome: '))
while len(nome) <= 3:
    nome = str(input('Nome: '))

idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade: '))

salário = float(input('Salário: R$'))
while salário < 0:
    salário = float(input('Salário: R$'))

sexo = str(input('Sexo [ F / M ]:')).upper()[0]
while sexo not in 'FM':
    sexo = str(input('Sexo [ F / M ]:')).upper()[0]

print('Agora informe seu estado civil - Digite S - Solteir(a), C - Casado(a), V - Viúvo(a) ou D - Divorciado(a)')
estcivil = str(input('Estado Civil: ')).upper()[0]
while estcivil not in 'SCVD':
    estcivil = str(input('Estado Civil: ')).upper()[0]
print('=-' * 30)
print(f'{"DADOS INFORMADOS:":.20}')
print('=-' * 30)
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R${salário:.2f}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {estcivil}')