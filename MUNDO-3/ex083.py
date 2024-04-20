'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
lista = []
n1 = (input('Digite a sua expressão usando "()": '))
for paren in n1:
    if paren == '(':
        lista.append('(')
    elif paren == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expresão válida!')
else: 
    print('Expressão inválida!')
    

