'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
idade18 = 0 
home = 0
mulherm = 0
while True:
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        home += 1
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 18:
        idade18 +=1
    if sexo == 'F' and idade < 20:
        mulherm +=1
    keep = ' '
    while keep not in 'SN':
        keep = str(input('Gostaria de continuar? [S/N]')).strip().upper()[0]
    if keep == 'N':
        break
print('\033[31mFim do cadastro\033[m')
print(f'''Quantidade de pessoas maiores de idade: {idade18}
Total de homens: {home}
Mulher(es) com menos de 20 anos: {mulherm}''')