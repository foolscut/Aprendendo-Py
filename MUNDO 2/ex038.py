'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais '''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
if n1 > n2:
    print('O priemiro valor digitado é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Não existe diferença entre os valores {} e {}'.format(n1,n2))
    