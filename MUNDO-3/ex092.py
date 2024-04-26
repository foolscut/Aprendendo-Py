'''Exercício Python 092:
Crie um programa que leia nome,ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
dados = dict()
dados['nome'] = str(input('Digite o nome: '))
idade = int(input('Digite o ano em que nasceu: '))
age = date.today().year - idade
dados['idade'] = age
dados['ctps'] = int(input('Digite o número da CTPS (0 caso não tenha): '))
if dados['ctps'] != 0:
    n1 = int(input('Digite o ano de contratação: '))
    dados['salario'] = int(input('Digite o valor do salário: '))
    aposenta = n1 + 35
    dados['aposenta'] = aposenta
    dados['idaposenta'] = (date.today().year - n1) + 35 + age
    print('-=-'*15)
    for k, v in dados.items():
        print(f'--{k} tem o valor {v}')
else:
    print('-=-'*15)
    print(f'Nome, {dados["nome"]} idade {dados["idade"]} anos e CTPS = {dados["ctps"]}')