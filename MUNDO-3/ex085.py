'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
lista = [[],[]]
for c in range(1,8):
    n1 = (int(input(f'Digite o {c}° valor: ')))
    if n1 % 2 == 0:
        lista[0].append(n1)
    else:
        lista[1].append(n1)
lista[0].sort()
lista[1].sort()
print('-='*20)
print(f'Essa é a lista de números digitada, divida em par e impar: {lista}')
print(f'Os valores pares são: {lista[0]}')
print(f'Os valores ímpares são: {lista[1]}')
    