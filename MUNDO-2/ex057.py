'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite seu sexo [M/F]')).upper()[0].strip()
while sexo not in 'MmFf':   
        sexo = str(input('Você não digitou uma opção válida. Digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado!'.format(sexo))    
