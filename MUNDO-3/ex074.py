'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
n1 = (randint(0,399)), (randint(0,399)), (randint(0,399)), (randint(0,399)), (randint(0,399))
print(f'Essa é a lista do números aleatórios: {n1}')
print(f'O maior valor é: {max(n1)}') # pega o maior número da variável
print(f'O menor valor é: {min(n1)}') # pega o menor número da variável
