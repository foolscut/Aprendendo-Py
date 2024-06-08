'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request 

try:
    site = urllib.request.urlopen('https://simoc.caixa/simoc/')
except:
    print('Deu erro!')
else:
    print('Tudo certo, acessei')