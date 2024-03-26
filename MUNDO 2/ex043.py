'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 34,9: Obesidade grau I
  35 até 39,9: Obesidade grau II
– Acima de 40: Obesidade grau III'''
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('De acordo com a sua altura de {} e peso de {}, seu IMC {:.2f} indica que você está \033[33mAbaixo do Peso\033[m'.format(altura,peso,imc))
elif imc <=25:
    print('De acordo com a sua altura de {} e peso de {}, seu IMC {:.2f} indica que você está \033[32mPeso Ideal\033[m'.format(altura,peso,imc))
elif imc <=30:
    print('De acordo com a sua altura de {} e peso de {}, seu IMC {:.2f} indica que você está \033[31mSobrepeso\033[m'.format(altura,peso,imc))
elif imc <= 40:
    print('De acordo com a sua altura de {} e peso de {}, seu IMC {:.2f} indica que você está \033[31mObesidade!\033[m'.format(altura,peso,imc))
else:
    print('De acordo com a sua altura de {} e peso de {}, seu IMC {:.2f} indica que você está \033[31mObesidade MORBIDA!!!!\033[m'.format(altura,peso,imc))
    