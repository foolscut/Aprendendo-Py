'''Exercício Python 094: Crie um programa que leia nome,
sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
dados = dict()
novosdados = []
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = (input('Digite o nome da pessoa: ')) # nome
    while True:
        dados['sexo'] = str(input('Digite o sexo (M/F): ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Caracter inválido! DIGITE "M" OU "F".')
    dados['idade'] = int(input('Digite a idade: '))
    soma += dados['idade']
    novosdados.append(dados.copy())
    while True:
        n1 = str(input('Quer Continuar? (S/N)')).upper()[0]
        if n1 in 'SN':
            break
        print('Caracter inválido! DIGITE "S" OU "N".')
    if n1 == 'N':
        break
media = soma / len(novosdados)
print(f'A) O total de pessoas cadastradas é: {len(novosdados)}')
print(f'B) A média de idade é {media}')
print(f'C) As mulheres cadastradas foram: ', end ='')
print('<<<Imprimindo informações>>>')
for p in novosdados:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}]',end ='')
print()
print(f'D) Lista de pessoas acima da média: ')
for p in novosdados:
    if p['idade'] >= media:
        print('     ',end = '')
        for k, v in p.items():
            print(f'{k} = {v}; ',end = '')
        print()
print('<<<<<FIM DO PROGRAMA>>>>>')
