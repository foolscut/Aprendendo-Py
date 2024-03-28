'''Crie um programa que mostre todos os numeros pares entre 1 e 50'''
print('Os números pares entre 0 e 50 são esses: ')
from time import sleep
for c in range(0,51, +2): #(2, 51 ,2):
    print(c)
    sleep(0.5)
print('É isso.')