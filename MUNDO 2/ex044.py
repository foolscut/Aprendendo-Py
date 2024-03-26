''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''
print('{:=^40} '.format (' LOJAS JESTER ')) #{:=^40} CENTRALIZA A MENSAGEM EM 40 ESPAÇOS
produto = float(input('Digite o valor do produto para que lhe mostremos nossas opções de pagamento: '))
print('ESCOLHA A FORMA DE PAGAMENTO!')
print('''[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')
pag = int(input('Digite a opção de pagamento que deseja: '))
print('O preço do seu produto é: R${}, nososs descontos são:'.format(produto))
if pag == 1:
    print('à vista dinheiro/cheque: 10% de desconto = R${}'.format((produto-(produto*10/100))))
elif pag == 2:
    print('à vista no cartão: 5% de desconto = R${}'.format(produto-(produto*5/100)))
elif pag == 3:
    print('em até 2x no cartão: preço formal = R${}, cada parcela'.format(produto/2))
elif pag == 4:
    parc = int(input('Digite em quantas vezes deseja parcelar: '))
    total = produto+(produto*20/100)
    parcelamento = total / parc
    print('Sua compra em {} parcelas no cartão: 20% de juros = R${:.1f}, cada parcela. Total de R${}'.format(parc,parcelamento,total))
else:
    print('Opção inválida, tente novamente!')
     