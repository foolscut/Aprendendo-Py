'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor = int(input('Digite o valor que deseja sacar: '))
total = valor
ced = 50
cedulas = 0
while True:
    if total >= ced:
        total -= ced
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'Total de {cedulas} cédula(s) de R${ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedulas = 0
        if total == 0:
            break
print('Volte sempre')

