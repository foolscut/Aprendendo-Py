'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
n1 = (int(input('Digite o 1° número: '))), (int(input('Digite o 2° número: '))), (int(input('Digite o 3° número: '))), (int(input('Digite o 4° número: ')))
print(f'Você digitou {n1}')
print(f'O número 9 apareceu {n1.count(9)} vez(es)')
if 3 in n1:
    print(f'O número 3 apareceu na {n1.index(3)+1}° posição')
else:
    print('O número 3 não foi digitado!')
for n in n1:
    if n % 2 == 0:
        print(f'Os números pares são: {n}')
