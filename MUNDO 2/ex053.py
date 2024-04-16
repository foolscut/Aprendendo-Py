'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
n1 = str(input('Digite uma frase:')).strip().upper()
pala = n1.split()
jun = ''.join(pala)
inv = jun[::-1]
'''inv = ''
for letra in range (len(jun)-1, -1, -1):
    inv += jun[letra] '''
print('O inverso de {} é {}.'.format(jun,inv))
if inv == jun:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo.')