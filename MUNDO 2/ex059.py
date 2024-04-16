'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''
from time import sleep
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
açao = 0
while açao != 5:
    print('\033[32mAgora escolha o que deseja fazer.\033[m')
    açao = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa '''))
    if açao == 1:
        soma = n1 + n2
        print('\033[33mA soma entre {} + {} é = {}\033[m'.format(n1,n2,soma))
    elif açao == 2:
        multi = n1 * n2
        print('\033[33mA multiplicação entre {} x {} é = {}\033[m'.format(n1,n2,multi))
    elif açao == 3:
        if n1 > n2:
            print('\033[33m{} é o maior valor digitado.\033[m'.format(n1))
        else:
            print('\033[33m{} é o maior valor digitado.\033[m'.format(n2))
    elif açao == 4:  
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
    elif açao == 5:
        print('\033[33mEncerrando...\033[m')
    else:
        print('\033[31mOpção inválida!\033[m')
    sleep(1.5)
print('Fim do programa, adios!')


