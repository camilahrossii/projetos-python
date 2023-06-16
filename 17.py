# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    user = str(input('Usuário: '))
    senha = str(input('Senha: '))
    if user != senha:
        print('Bem-vindo(a)!')
        break
    if user == senha:
        print('ERRO! A senha não pode ser igual ao nome de usuário. Tente novamente.')