'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
print('-'*30)
print('Vamos jogar PAR OU IMPAR')
print('-'*30)
v = 0
while True:
    n1 = int(input('Digite um número: '))
    pc = randint (0,10)
    total = n1 + pc
    n2 = ' '
    while n2 not in 'pi':
        n2 = str(input('Você quer IMPAR OU PAR? [I/P]'))
    print(f'Você jogou {n1} e o computador jogou {pc}, total é {total} ', end='')
    print('\033[33mDeu PAR!\033[m' if total % 2 == 0  else '\033[33mDeu IMPAR\033[m'  )
    if n2 == 'p':
        if total % 2 == 0:
            print('\033[32mVocê ganhou!\033[m')
            v += 1
        else:
            print('\033[31mVocê perdeu!\033[m')
            break
    if n2 == 'i':
        if total % 2 == 1:
            print('\033[32mVocê ganhou!\033[m')
            v += 1
        else:
            print('\033[31mVocê perdeu!\033[m')
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER! Você venceu \033[33m{v}\033[m vez(es).')
