'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = []
for c in range(0,5):
    n1 = (int(input(f'Digite o {c}° número ')))
    if c == 0 or n1 > lista[-1]:
        lista.append(n1)
        print('Número adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n1 <= lista[pos]:
                lista.insert(pos, n1)
                print(f'Número adicionado na posição {pos}')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitasdos são: {lista}')