'''16 Crie um programa que leia um numero real e mostre na tela a sua porção inteira
n1 = float(input('Digite um número real que contenha (Virgula): '))
print('O número que você digitou {}, sua parte inteira é {:.0f}' .format (n1, n1)) # (n1, math.trunc(n1))'''

'''#17Programa que leia as medidas do cateto oposto e do adjacente e mostre o valor da hipotenusa
from math import hypot
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente:'))
n3 = hypot (n1, n2)
print('O valor da hipotenusa do triangulo retangulo é: ', n3)'''

'''#18 Leio o valor de um angulo qualquer e mostre seu seno, cosseno e a tangente
from math import sin, cos, tan, radians
n1 = float(input('Digite o valor de um angulo: '))
seno = sin(radians(n1))
cosseno = cos(radians(n1))
tangente = tan(radians(n1))
print('O angulo de {}° tem seu seno igual à: {:.2f}'.format(n1, seno))
print('O angulo de {}° tem seu cosseno igual à: {:.2f}'.format(n1, cosseno))
print('O angulo de {}° tem sua tangente igual à: {:.2f}'.format(n1, tangente))'''

'''#19 Crie um programa que escolha um nome aleatorio, entre 4 nomes
from random import choice
a1 = str(input('Digite o nome do primeiro aluno(a): '))
a2 = input('Digite o nome do segundo aluno(a): ')
a3 = input('Digite o nome do terceiro aluno(a): ')
a4 = input('Digite o nome do quarto aluno(a): ')
lista = [a1,a2,a3,a4]
escolhido = choice(lista) #choice escolhe um dos
print('O(a) aluno(a) sorteado(a) foi: {}'.format (escolhido))'''

'''#20 Baseado no exercicio anterior, crie um sortei que mostre todos em ordem
from random import shuffle
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do teceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1,a2,a3,a4]
shuffle (lista) #shuffle embaralha e apresenta todos 
print('A ordem de apresentação do trabalho é: ', lista)'''

'''#21 tocando um .mp3
import pygame
pygame.init()
pygame.mixer.music.load(elaqueeuamo.mp3)
pygame.mixer.music.play()
pygame.event.wait'''

#22  len(), conta a quantidade de str em uma frase
# count(), contar a quantidade
#  find(), encontrar
#  transformações com replace(), substituir
#  upper(), letra maiúscula
#  lower(), letra minúscula
#  capitalize(), Só a primeira letra fica maiúscula, o resto fica min
#  title(), toda palavra após um espaço fica com a primeira letra maiuscula
#  strip(), remove os espaços do começo e do final da str
#  rstrip(), remove os espaços do final da str
#  lstrip(), remove os espaços do começo da str
#  junção com join(). junta as str, processo reverso do split, e pode preencher os epaços com algum valor '-'
#  frase.split() divide a str em uma lista, onde cada palavra tem um numero e dentro de cada palavra as letras tem numeros que começam com 0
'''frase = 'Curso em vídeo é muito foda mano'
print (frase[::2])'''

#22programa que lê o nome completo e da algumas informações
'''nome = str(input('Digite seu nome completo: ')).strip()
n2 = nome.split()
print('Seu nome completo em letras maiúsculas:', nome.upper())
print('Seu nome completo em letras minúsculas:', nome.lower())
print('Seu nome tem um total de {} letras.'.format (len(nome) - nome.count (' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format (n2[0], len(n2[0])))'''


#23 leia um numero de 0 a 9999 e mostre na tela cada um dos numeros separados
'''n1 = int(input('Digite um número com no máximo 4 digitos, ex: 1234:'))
print('Você digitou: ', n1)
u = n1//1%10
d = n1//10%10
c = n1//100%10
m = n1//1000%10
print('Sua unidade é: {}'.format(u))
print('Sua dezena é: {}'.format(d))
print('Sua centena é: {}'.format(c))
print('Seu milhar é: {}'.format(m))'''

#24 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''from gettext import find
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('Analisando se sua cidade começa com a palavra SANTO...')
print(cidade[:5].upper() == 'SANTO')'''

#25 Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” 
'''nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome contém SILVA? {}'.format ('silva' in nome.lower()))'''

#26 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#  em que posição ela aparece a primeira vez e
#  em que posição ela aparece a última vez.
'''a = str(input('Digite uma frase qualquer: ')).strip().lower()
print('A frase que você digitou, contem {} letra(s) "a"'.format(a.count('a')))
print('A primeira letra "a" aparece na {}° posição'.format(a.find('a')+1)) 
print('A ultima letra "a" aparece na {}° posição'.format(a.rfind('a')+1))'''

#27 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
'''nome = str(input('Digite seu nome completo: ')).strip()
a = nome.split()
print('Seu primeiro nome é: {}'.format(a[0]))
print('Seu úlltimo nome é {}:'.format(a[len(a)-1]))'''

#condicionais 
    #if carro.esquerda(): 
    # bloco True
    #else: 
    # bloco False

'''nome = str(input('Digite seu nome: ')).lower()
if nome == 'iuri': #Quando for uma palavra, deve-se colocar a palavra que ira ser separada entre ' '
    print('Noossssaaa, que nome top!')
else:
    print('Seu merda, nome paia')
print('Prazer!')'''



