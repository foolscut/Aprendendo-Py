'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
from datetime import date
somaidade = 0
medidade = 0
homevelho = 0
nomevelho = ''
totmulher = 0
for n in range(1,5):
    print('------ {}° Pessoa ------'.format(n))
    nome = str(input('Digite o nome: '.format(n)))
    idade = int(input('Digite a idade: '.format(n)))
    sexo = str(input('Digite o sexo. M para masculino e F para feminino: '.format(n))).strip()
    somaidade += idade
    if n == 1 and sexo in 'Mm':
        homevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homevelho:
        homevelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
medidade = somaidade / 4
print('A média da idade das pessoas é {:.1f}'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}'.format(homevelho,nomevelho))
print('São {} mulheres com menos de 20 anos de idade.'.format(totmulher))

'''idade = date.today().year - idade
media = idade'''
