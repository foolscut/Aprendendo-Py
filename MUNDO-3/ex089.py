'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
from time import sleep
lista = []
qtd = 0
while True:
    nome = (input('Digite o nome do aluno: '))
    n1 = (float(input('Digite a 1° nota: ')))
    n2 = (float(input('Digite a 2° nota: ')))
    media = (n1 + n2) / 2
    lista.append([nome,[n1,n2],media])
    parar = ' '
    if parar not in 'NS':
        parar = str(input('Quer continuar? ')).upper().strip()[0]
        if parar == 'N':
            break
print('-='*20)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>7}')
print('-='*20)
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*20)
    qual = int(input('Qual aluno você quer ver as notas? (999 interrompe.): '))
    if qual == 999:
        break
    if qual <= len(lista)-1:
        print(f'As notas do aluno {lista[qual][0]} são: {lista[qual][1]}')

print('FINALIZANDO...')
sleep(1)
print('ADIOS!')
        
    
    
    
    