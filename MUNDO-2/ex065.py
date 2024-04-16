'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
keep = 'S'
soma = qtd = media = maior = menor = 0
while keep in 'sS':
    n1  = int(input('Digite um número: '))
    soma += n1
    qtd += 1
    if qtd == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    keep  = str(input('Gostaria de continuar [S/N]? ')).upper().strip()[0]
    media = soma / qtd
print(f'Você digitou {qtd} números e a media deles é {media}')
print(f'Dos números digitados, {maior} é o maior e {menor} é o menor')
    
