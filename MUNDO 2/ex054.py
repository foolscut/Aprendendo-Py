'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
contma = 0
contme = 0

for c in range(1,8):
    data = int(input('Digite a data de nascimento da {}° pessoa: '.format(c)))
    id = date.today().year - data
    if id >=18:
        contma += 1
    else:
        contme += 1
print('Ao todo temos {} pessoa(s) maior(es) e {} pessoa(s) menor(es).'.format(contma,contme))