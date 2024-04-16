'''faça um programa que calcule a soma entre todos os numeros impares,
que são multiplos de 3 e que se encontrem no intervalo entre 1 até 500'''
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        contador = contador + 1
print('A soma de todos os {} números impares e multiplos de três é: {}'.format(contador,soma))