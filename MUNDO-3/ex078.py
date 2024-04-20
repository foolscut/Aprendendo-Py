'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
lista = []
menor = 0
maior = 0
for captura in range(0,5):
    lista.append(int(input(f'Digite o {captura}° número: ')))
    if captura == 0:
        maior = menor = lista[captura]
    else:
        if lista[captura] > maior:
            maior = lista[captura]
        if lista[captura] < menor:
            menor = lista[captura]
print('-='*35)
print(f'Você digitou os valores: {lista}')
print(f'O maior número digitado foi: {maior} que esta na(s) posição(ções): ',end = '')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end = '')
print()
print(f'O menor número digitado foi: {menor} que esta na(s) posição(ções): ',end = '')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end = '')
