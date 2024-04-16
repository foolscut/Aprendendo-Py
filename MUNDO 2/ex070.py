'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. '''
total = soma = maisde1000 = maisbarato = cont =  0
barato = ' '
while True:
    nomeproduto = str(input('Digite o nome do produto: '))
    preçoproduto = int(input('Digite o valor do produto: R$'))
    total += preçoproduto
    keep = ' '
    cont +=1
    if cont == 1 or preçoproduto < maisbarato:
        maisbarato = preçoproduto
        barato = nomeproduto
    if preçoproduto >= 1000:
        maisde1000 +=1
    while keep not in 'SN':
        keep = str(input('Gostaria de continuar [S/N]: ')).strip().upper()[0]
    if keep == 'N':
        break
print(f'Total gasto na compra: \033[31mR${total:.2f}\033[m')
print('='*30)
print(f'Total de produtos que custam mais de R$1000: {maisde1000}')
print('='*30)
print(f'O produto mais barato foi \033[32m{barato}\033[m e custa R${maisbarato}')
print('='*30)