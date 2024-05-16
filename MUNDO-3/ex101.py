'''Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(ano):
    from datetime import date
    data = date.today().year
    idade = data - nascimento
    if idade < 16:
        return f'Com {idade} anos de idade, o voto é NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos de idade, o voto é OPCIONAL'
    else:
        return f'Com {idade} de idade, o voto é OBRIGATÓRIO'


nascimento = int(input('Em que ano você nasceu: '))    
print(voto(nascimento))






