'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
dt = n1 + (10-1) * n2 #DÉCIMA RAZÃO
for c in range(n1 ,dt + n2, n2):
    print('{}'.format(c), end= ' → ')
print('Fim!')