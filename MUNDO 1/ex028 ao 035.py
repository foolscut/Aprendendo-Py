#28 Jogo de adivinhação
'''from random import randint
from time import sleep
n1 = int(input('Digite um número entre 0 e 5, tentando adivinhar qual eu escolhei: '))
print('PROCESSANDO...')
sleep(3)
pc = randint (0,5)
if n1 == pc:
    print('Parabéns, você escolheu o mesmo número que eu!')
else: print('Ganhei de você, eu pensei no número {} e você no número {}'.format (pc, n1))'''


#29 Ler a velocidade de um carro e aplicar multa de R$7 para cada KM a mais da velocidade permitida 80KM/h
'''from time import sleep
n1 = int(input('Digite a velocidade que o carro pasou pelo radar:'))
print('Verificando a velocidade em que o carro passou...')
sleep(2)
if n1<=80:
    print('Velocidade regular, diriga sempre com atenção!')
else:
    print('A velocidade de {} KM/H ultrapassa o limite permitido, multa de R${} aplicada!'.format (n1,((n1-80)*7)))'''

#30 Mostra se o numero digitado é par ou impar
'''n1 = int(input('Digite um numero qualquer:'))
n2 = n1 % 2
if n2 == 0:
    print('O número {} é PAR'.format(n1))
else:
    print('O numero {} é IMPAR'.format(n1))'''

#31 Calculador de de custo de viagem
'''n1 = int(input('Digite a distância de sua viagem em KM:'))
if n1<=200:
    print('Baseado na distância de {}, o valor da sua passagem é: R${}'.format(n1, n1*0.50))
else: print('Baseado na distancia de {}, o valor da sua passagem é: R${}'.format(n1,n1*0.45))'''

#32 Identificador de ano bissexto
'''from datetime import date
n1 = int(input('Digite o ano que quer analisar ou digite 0 para analisar o ano atual: '))
if n1 == 0:
    n1 = date.today().year
if n1 % 4 ==0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(n1))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(n1))'''

#33 Maior e menor valores
'''a = int(input('Digite um número:'))
b = int(input('Digite um outro número:'))
c = int(input('Digite mais um número:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O numero maior é:',maior)
print('O número menor é:',menor)'''

#34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
'''n1 = float(input('Digite o valor do seu salário: '))
n2 = n1*0.10
n3 = n1*0.15
if n1 >= 1250:
    print('Você teve um reajuste salarial de 10%, seu antigo salário era R${} e agora é R${:.2f}'.format(n1,n1 + n2))
else:
    print('Você teve um reajuste salarial de 15%, seu antigo salário era R${} e agora é R${:.2f}'.format(n1, n1+n3))'''

#35 Analisador de triangulo
'''print('-=-'*21)
print('Analisador de triangulo')
print('-=-'*21)
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os valores digitados PODEM FORMAR um triangulo!')
else:
    print('Os valores digitados NÃO PODEM formar um triangulo')'''
