'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = []
rendimento = {}
saldo = []
while True:
    rendimento.clear()
    rendimento['nome'] = str(input('Digite o nome do jogador: '))
    n1 = int(input('Quantas partidas participou? '))
    saldo.clear()
    for c in range (0,n1):
        saldo.append(int(input(f'Quantos gols foram feitos na {c + 1} partida? ')))
    rendimento['gols'] = saldo[:]
    rendimento['total'] = sum(saldo)
    time.append(rendimento.copy())
    while True:
        pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if pergunta in 'SN':
            break
        print('Digite apenas "S" ou "N"')
    if pergunta == 'N':
        break
print('-='*30)
for i in rendimento.keys():
    print(f'{i:<15}',end ='')
print()
print('-='*30)  
for k, v in enumerate(time):
    print(f'{k:3>}  ',end ='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)   
while True:
    busca = int(input('Digite a chave do jogar que quer buscar? (999 para sair): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro, jogador não encontrado!')
    else:
        print(f'== LEVANTAMENTO do JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
                    print(f'    No jogo {i+1} fez {g} gols.')
    print('-='*30)
print('Fim, caraio!')                