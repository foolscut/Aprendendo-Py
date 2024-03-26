'''Escreva um programa em Python que leia um número inteiro qualquer e
 peça para o usuário escolher qual será a base de conversão:
   1 para binário, 2 para octal e 3 para hexadecimal. '''

numero = int(input('Digite um número inteiro qualquer: '))
print('Escolha sua base de conversão.')
con = int(input('''Digite:
\033[1;31m[1]\33[m para binário
\033[1;31m[2]\033[m para octal
\033[1;31m[3]\033[m para hexadecimal '''))
#oct = 
#hexa = 
if con == 1:

    print('A conversão de {} para BINÁRIO é {}'.format(numero, bin(numero)[2:]))
elif con == 2:
    print('A conversão de {} para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif con == 3:
    print('A conversão de {} para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Você não digitou uma opção válida!')