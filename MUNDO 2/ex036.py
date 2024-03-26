'''36 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. '''

casa = float(input('Digite o valor da casa que deseja comprar: '))
sal = float(input('Digite o valor do seu salário: '))
parcelas = int(input('Digite em quantos anos você deseja parcelar: '))
ptr = sal * 0.3
mensalidade = casa / (parcelas*12)

if mensalidade > ptr:
    print('Seu emprestimo foi negado, o valor da prestação representa mais de 30% do seu salário')
else:
    print('Seu empréstimo foi aprovado!')
