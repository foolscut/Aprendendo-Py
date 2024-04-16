'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes '''

print('-=-'*21)
print('Analisador de triângulo')
print('-=-'*21)
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os valores digitados PODEM FORMAR um triangulo!')
    if n1 == n2 == n3:
        print('Esse é um triângulo EQUILÁTERO, todos os seus lados são iguas')
    elif n1 != n2 != n3 != n1:
         print('Esse triângulo é ESCALENO, todos seus lados são diferentes')
    else:
        print('Esse é um triângulo ISÓSCELES, doi dos seus lados são iguas')
else:
    print('Os valores digitados NÃO PODEM formar um triangulo')
