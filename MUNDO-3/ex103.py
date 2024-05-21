'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome='-Desconhecido-', gols= 0):
    print(f'O jogador {nome} fez {gols} gol(s)')

    

n1 = str(input('Digite o nome do jogador: '))
n2 = str(input('Digite quantos gols ele fez: '))
if n2.isnumeric():
    n2 = int(n2)
else:
    n2 = 0
if n1.strip() =='':
    ficha()
else:
    ficha(n1,n2)
