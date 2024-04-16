'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
n1 = 0
qtd = 0
soma = 0
n1 = int(input('Digite um valor: '))
while n1 != 999:
    soma += n1
    n1 = int(input('Digite mais um valor [999 para encerrar]:'))
    qtd += 1
    
print('Você digitou {} números, a soma deles é {}'.format(qtd,soma))