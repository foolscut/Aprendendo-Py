''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''

n1 = int(input('Digite um número: '))
tot = 0
for c in range(1,n1 + 1):
    if n1 % c ==0:
        print('\033[32m',end =' ')
        tot += 1
    else:
        print('\033[31m',end =' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n1,tot))
if tot == 2:
    print('O número {} é um número primo'.format(n1))
else:
    print('O número {}, não é um número primo.'.format(n1))