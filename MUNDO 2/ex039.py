'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
n1 = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - n1 
print('Você tem {} anos de idade'.format(idade))
if idade < 18:
    print('Você ainda não completou 18 anos de idade, você deve se alistar em {}'.format(n1+18))
    print('Você deve se alistar daqui {} anos'.format((18 - idade)))
elif idade > 18:
    print('Você já passou da idade de se alistar, você deveria ter se alistado em {}'.format(n1+18))
    print('Você passou {} anos da idade de se aliastar'.format((idade - 18)))
elif idade == 18:
    print('Você esta na idade de se alistar, vá até a junta militar mais próxima de sua cidade!')