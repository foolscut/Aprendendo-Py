'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint  
from time import sleep
print('{:=^40} '.format(' Vamos jogar PEDRA PAPEL e TESOURA '))
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
n1 = int(input('Digite uma opção:'))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = randint(0, 2)
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('Você jogou {}. A máquina jogou {}'.format(lista[n1],lista[maquina])) 
if maquina == 0: #MÁQUINA JOGA PEDRA
    if n1 == 0:
        print('EMPATE')
    elif n1 == 1:
        print('Você VENCEU')
    elif n1 == 2:
        print('Maquina Venceu')
    else:
        print('Opção invalida')    
 
elif maquina == 1: #MAQUINA JOGA PAPEL
    if n1 == 0:
        print('Maquina VENCEU')
    elif n1 == 1:
        print('EMPATE')
    elif n1 == 2:
        print('Você venceu')
    else:
        print('Opção invalida')    
   
elif maquina == 2: #MAQUINA JOGA TESOURA
    if n1 == 0:
        print('Você VENCEU')
    elif n1 == 1:
        print('Maquina VENCEU')
    elif n1 == 2:
        print('EMPATE')
    else:
        print('Opção invalida')



