'''Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.'''

from ex107 import moeda

p = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 22% de {moeda.moeda(p)} temos: {moeda.moeda(moeda.aumeta(p,22))}')
print(f'Diminuindo 15% de {moeda.moeda(p)} temos: {moeda.moeda(moeda.diminui(p,15))}')