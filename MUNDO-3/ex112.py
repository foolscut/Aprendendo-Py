'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''

from ex111.utilidadescev.moeda import moeda
from ex111.utilidadescev.dado import dado

p = dado.leiadinheiro('Digite um valor: R$')
moeda.resumo(p,35,22)