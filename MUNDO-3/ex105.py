'''Exercício Python 105: Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:

Quantidade de notas
A maior  nota
A menor nota
A média da turma
A situação (opcional)'''
def notas(*num, situ = False):
    """
    => Funcao para analisar varias notas e fornecer alguns parametros;
    -situ = funcao opcional, para mostrar ou nao a funcao 'situacao' 
    -total = mostra a quantidade notas inseridas
    -maior = mostra a maior nota, usando max
    -menor = mostra a menor nota, usando min
    -media = mostra a soma das notas dividido pela quantidade de notas inseridas
    -situacao = caso True, mostra os dados, caso False nao mostra
    """
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if situ:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5,5,5,7.8,6.6,9.8,situ=False)
help(notas)