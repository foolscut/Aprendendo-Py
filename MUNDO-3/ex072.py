'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

keep =' '
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n1 = int(input('Digite um valor de 0 a 20 para ver ele por extenso: '))
    if 0 <= n1 <=20:
        print(f'Você digitou: {extenso[n1]}')
    keep = str(input('Você quer continuar? [S/N]? ')).upper().strip()[0]   
    while keep not in 'NS':              
        if keep == 'N':
            break     
    print('Adios!')
