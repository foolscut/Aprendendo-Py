'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
from time import sleep
c = 1
n1 = int(input('Digite um número entre 0 e 10, tentando adivinhar qual eu escolhei: '))
pc = randint (0,10)
while n1 != pc:
    n1 = int(input('Tente novamente: '))
    c += 1
    if n1 == pc:
        print('Parabéns, você escolheu o mesmo número que eu!') 
    else:
        if n1 > pc:
            print('Menos')
        elif n1 < pc:
            print('Mais')
           
print('Você precisou de {} tantativa(s) para acertar.'.format(c))