'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO'''
n1 = float(input('Digite o valor da sua primeira nota: '))
n2 = float(input('Digite o valor da sua segunda nota: '))
med = (n1+n2)/2
print('Sua média é {}'.format(med))
if med < 5:
    print('\033[31mREPROVADO\033[m')
elif med <=5 or med <= 6.9:
    print('\033[33mRECUPERAÇÃO\033[m')
elif med >= 7:
    print('\033[32mAPROVADO\033[m')