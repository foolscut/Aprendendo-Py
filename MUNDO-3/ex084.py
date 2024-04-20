'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

lista = list()
lista2 =list()
maior = menor = 0
while True:
    lista2.append(str(input("Digite o nome da pessoa: ")))
    lista2.append(float(input('Digite o peso da pessoa: ')))
    if len(lista) == 0:
          maior = menor = lista2[1]
    else:
        if lista2[1] > maior:
            maior = lista2[1]
        if lista2[1] < menor:
             menor = lista2[1]
    lista.append(lista2[:])
    lista2.clear()
    resp = input('Gostaria de continuar? S/N ').upper().strip()[0]
    if resp in 'Nn':
            break
print('-='*30)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maior} KG, peso de ',end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ',end ='')
print()
print(f'O menor peso foi de {menor}KG, peso de ',end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')
print()
          
