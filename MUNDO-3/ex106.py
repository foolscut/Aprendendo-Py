'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
'''
from time import sleep

c = ('\033[m',          # 0 sem cores
     '\033[0;30;41m',   # vermelho
     '\033[0;30;42m',   # verde
     '\033[0;30;43m',   # amarelo
     '\033[0;30;44m',   # azul
     '\033[0;30;45m',   # roxo
     '\033[7;30m',      # branco
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[0],end='')
    print(c[7],end='')
    help(com)
    print(c[0],end='')
    sleep(2)

def titulo(msg, cores=0):
    tam = len(msg)+4
    print(c[cores],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('Função ou bibliotéca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)    