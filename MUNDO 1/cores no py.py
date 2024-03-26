'''\033[style,text,back m '''

'''códigos para style: 0 normal
1 negrito
4 sublinhado
7 negative '''

'''Códigos para a cor das letras
30 branco
31 vermelho
32 verde
33 amarelho
34 azul
35 roxo
36 oceano
37 cinza '''

'''Códigos para a cor de fundo, mesmo esquema das cores das letras
40
41
42
43
44
45
46
47 

print('\033[0;30;41mTeste\033[m') '''

#lista de cores
'''nome = str(input('Digite seu nome: '))
cores = {'limpa' :'\033[m',
          'azul' : '\033[34m',
           'amarelo' : '\033[33m',
            'pretoebranco' : '\033[7;30m' }

print('Olá {}{}{}, é com grande satisfação, que lhe dou os parabéns por chegar até aqui!'.format(cores['amarelo'],nome,cores['limpa']))'''

x = 'curso de python no cursoemvideo'
print(x[:5])