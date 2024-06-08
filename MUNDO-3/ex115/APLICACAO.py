'''Exercício Python 115a: Vamos criar um menu em Python, usando modularização.'''
from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
       #OPÇÃO DE LISTA O CONTEUDO DE UM ARQUIVO
       lerArquivo(arq)
    elif resposta == 2:
       #OPÇÃO PARA CADASTRAR UMA PESSOA NOVA
       cabeçalho('NOVO CADASTRO')
       nome = str(input('Nome: '))
       idade = leiaInt('Idade: ')
       cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

