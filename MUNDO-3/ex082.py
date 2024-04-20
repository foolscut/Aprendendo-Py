'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
lista1 = []
lista2 = []
while True:
    n1 = int(input('Digite um número: '))
    lista.append(n1)
    if n1 % 2 == 0:
        lista1.append(n1)
    else:
        lista2.append(n1)
    end = ' '
    if end not in 'NS':
        end = str(input('Quer continuar?')).upper().strip()[0]
        if end == 'N':
            break
print(f'Temos na lista principal, os números: {lista}')
print(f'Temos na lista de números pares, os números: {lista1}')
print(f'Temos na lista de números impares, os números: {lista2}')
    