'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''

'''n = int(input('Digite o número que deseja ver a tabuada: '))
for c in range(1,11):
    print('{} x {:2}= {}'.format(n, c, n*c)) '''

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 20)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 20)
print('FIM DA TABUADA')
