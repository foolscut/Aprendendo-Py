'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. '''

n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end= ' → ')
        termo += n2
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer ver? '))
print('Progressão finalizada com um total de {} termos mostrados'.format(total))


'''print('Gerador de PA')
print('-='*10)
primeiro = int(input('Digite o 1° termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end = '')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Digite quanto mais termos você quer ver: '))
print('FIM!')'''