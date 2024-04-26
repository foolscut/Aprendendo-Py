'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
ranking = {}
jogadores = {'Jogador-1':randint(1,6),
             'Jogador-2':randint(1,6),
             'Jogador-3':randint(1,6),
             'Jogador-4':randint(1,6)}
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v}')
print('-='*20)
print('     COLOCAÇÃO       ')
print('-='*20)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}° o {v[0]} com dado de valor {v[1]}')

