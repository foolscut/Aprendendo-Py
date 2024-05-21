'''Exercício Python 104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(msg):
    valida = False
    valor = 0
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            valor = int(n1)
            valida = True
        else:
            print('\033[31mERRO! Digite um número inteiro!\033[m')
        if valida:
            break
    return valor


n1 = leiaInt('Digite um número: ')
print(f'Você digitou: {n1}')

