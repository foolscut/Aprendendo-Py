'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

lista = [[0,0,0],[0,0,0],[0,0,0]]
maior = pares = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = (int(input(f'Digite um valor para [{l} , {c}]')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]',end ='')
        if lista[l][c] % 2 == 0:
            pares += lista[l][c]
    print()
print('-='*20)
print(f'A soma dos valors pares é : {pares}')
print(f'A somas dos valores da 3° coluna é: {lista[0][2]+lista[1][2]+lista[2][2]}')
for c in range(0,3):
    if c == 0:
        maior = lista[1][c]
    elif lista[1][c] > maior:
        maior = lista[1][c]
print(f'O maior valor da segunda linha é: {maior}')
