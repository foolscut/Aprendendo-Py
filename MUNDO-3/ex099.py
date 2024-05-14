'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*num):
    contador = maior = 0
    for valor in num:
        if contador == 0:
            maior == valor
        else:
            valor > maior
            maior = valor
        contador += 1
    print('-='*20)
    print(f'''Recebi os números {num}
Com um total de {contador} digitos,
E o maior valor é {maior}''')

maior(1,5,6,7,8,9)
maior(1,5,7,10,250)
maior(100,1,2,3,4)
maior( )