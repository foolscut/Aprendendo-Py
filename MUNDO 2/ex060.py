'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''
from math import factorial
n1 = int(input('Digite um número: '))
c = n1
print('Calcucalando {}! = '.format(n1), end='')
while c > 0:
    print('{}'.format(c), end = '')
    c -= 1
    print(' x ' if c > 1 else ' = ', end= '')
print('{}'.format(factorial(n1)))
    
