'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
resultado = {}
resultado['Nome'] = str(input('Digite o nome do aluno: '))
resultado['Média'] = float(input(f'Digite a média de {resultado["Nome"]}: '))
if resultado['Média'] >= 7:
    resultado['Situação'] = 'Aprovado!'
elif 5 <= resultado['Média'] < 7:
    resultado['Situação'] = 'Recuperação!'
else:
    resultado['Situação'] = 'Reprovado!' 
print('-='*20)
for k, v in resultado.items():
    print(f'- {k} é {v}')
#print(f'O aluno {resultado["nome"]} tem média {resultado["media"]} e sua situação é {resultado["Situação"]}')