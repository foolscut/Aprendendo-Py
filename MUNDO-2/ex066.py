'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
n1 = cont = soma = 0
while n1 != 999:
    n1 = int(input('Digite um valor: '))
    if n1 == 999:
        break
    cont +=1 
    soma += n1
print('Fim do programa')
print(f'Você digitou {cont} números e a soma deles é {soma}')

