'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada'''
from time import sleep
def contador(i, f, p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print(f'Contar de {i} até {f} de {p} em {p}')
    print('-='*20)
    sleep(1.5)
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f'{cont} ',end ='',flush=True)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont} ',end='',flush=True)
            cont -= p
        print('FIM')
    
#principal
contador(1,10,1)
contador(10,0,2)
print('Personalize sua contagem!')
ini = int(input('Digite o inicio: '))
final = int(input('Digite o final: '))
passe = int(input('Digite o passe: '))
contador(ini,final,passe)