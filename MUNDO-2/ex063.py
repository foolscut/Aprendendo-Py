'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 - 1 - 1 - 2 - 3 - 5 - 8 '''
from time import sleep
n = int(input('Quantos termos você quer mostrar? '))
print('Analisando a Sequência de Fibonacci do número {}...'.format(n))
sleep(1.5)
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2),end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print('→ FIM')