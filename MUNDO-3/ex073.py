'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians',
        'Criciúma','Cruzeiro','Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio',
        'Internacional', 'Juventude', 'Palmeiras', 'Bragantino','São Paulo',
        'Vasco da Gama','EC Vitória')
print('='*100)
print('BRASILEIRÃO SÉRIE A')
print('='*100)
print(f'Lista de times: {times}')
print('='*100)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('='*100)
print(f'Os 4 ultimos times são: {times[-4:]}')
print('='*100)
print(f'O time do Chapecoense não está na lista dos 20 times') #{times.index("Chapecoense")+1}° posição')