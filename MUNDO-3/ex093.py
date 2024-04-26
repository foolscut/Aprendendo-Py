'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.'''
rendimento = {}
saldo = []
rendimento['nome'] = str(input('Digite o nome do jogador: '))
n1 = int(input('Quantas partidas participou? '))
for c in range(0,n1):
    saldo.append(int(input(f'Quantos gols foram feitos na {c+1} partida? ')))
rendimento['gols'] = saldo[:]
rendimento['total'] = sum(saldo)
print('-='*30)
print(rendimento)
print('-='*30)
for k, v in rendimento.items():
    print(f'O item {k} tem valor {v}')
print('-='*30)
print(f'O jogador {rendimento["nome"]} jogou {n1} partidas')
for i, v in enumerate(rendimento['gols']):
    print(f'na partida {i+1}, fez {v} gol(s)')
print(f'Foi um total de {rendimento["total"]} gol(s)')



