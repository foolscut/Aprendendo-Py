'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                              A) Quantos números foram digitados.                                                                                                           B) A lista de valores,ordenada de forma   decrescente.                                                                            
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
qtd = 0
while True:
    n1 = int(input('Digite um número: '))
    lista.append(n1)
    qtd +=1
    cont = ' '
    if cont not in 'NS':
        cont = (str(input('Quer continuar? S/N: '))).upper().strip()[0]
        if cont == 'N':
            break
lista.sort(reverse=True)
print('=+='*20)
print('Fim!')
print(f'Quantidade de números digitados: {qtd}')
print('=+='*20)
print(f'A lista em ordem descrescente: {lista}')
print('=+='*20)
if 5 in lista:
    print('O número 5 \033[32mfoi\033[m digitado')
else: 
    print('O número 5 \033[31mnão foi\033[m digitado')
print('=+='*20)