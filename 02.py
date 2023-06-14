# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
print('~ Vamos calcular o tempo aproximado de download de seu arquivo ~')
arquivo = float(input('Tamanho do arquivo (MB): '))
internet = float(input('Velocidade de Internet (Mbps)'))
calc = (arquivo /  internet) * 60
print(f'O tempo aproximado do download é de {calc:.0f} minutos.')
