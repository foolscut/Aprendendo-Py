'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint
from time import sleep
def sortea(lista):
    print('Realizando sorteio...',end = '')
    for cont in range (0,5):
        n = randint(1,10)
        lista.append(n)
        sleep(0.5)
        print(f'{n} ',end = ' ', flush=True)
    print('-=FIM=-')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares da lista: {lista} é {soma}')

numeros = []
sortea(numeros)   
somapar(numeros)   
