'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
dt = n1 + (10-1) * n2 #DÉCIMA RAZÃO
termo = n1
cont = 1
while cont <= 10:
    print('{}'.format(termo), end= ' → ')
    termo += n2
    cont += 1
print('Fim!')