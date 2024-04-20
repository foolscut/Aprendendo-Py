'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
while True:
    num = (int(input('Digite um número:')))
    if num not in lista:
        lista.append(num)
        print('Número adicionado')
    else:
        print('Número não adicionado, já foi digitado')
    continua = ' '
    if continua not in 'SN':
        continua = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if continua == 'N':
        break
lista.sort()
print(f'Você digitou os números {(lista)}')
print('Fim')

