'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(),
diminuir(),
dobro() e
metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

p = float(input('Digite um valor: '))
print(f'O dobro de {p} é: {moeda.dobro(p)} ')
print(f'A metade de {p} é: {moeda.metade(p)}')
print(f'Aumentando 22% de {p} temos: {moeda.aumeta(p,22)}')
print(f'Diminuindo 15% de {p} temos: {moeda.diminui(p,15)}')