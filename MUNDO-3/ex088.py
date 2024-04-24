from random import randint
from time import sleep
lista = []
lista2 = []
contador = 0
c = 1
qtdjogos = 1
print('-='*20)
print('     RANDOMIZADOR DE JOGOS DA MEGA       ')
print('-='*20)
n1 = int(input('Quantos jogos deseja fazer?'))
while qtdjogos <= n1:
    contador = 0
    while True:
        numeros = randint(1,60)
        if numeros not in lista:
            lista.append(numeros)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    lista2.append(lista[:])
    lista.clear()
    qtdjogos += 1 
print('-='*3, f'Sorteando {n1} jogos','-='*3)
for i, l in enumerate(lista2):
    print(f'Jogo {i+1}: {l}')
    sleep(1.5)