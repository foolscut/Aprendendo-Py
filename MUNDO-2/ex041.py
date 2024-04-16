'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER '''
from datetime import date
idade = int(input('Digite o ano em que você nasceu: '))
idade2 = date.today().year  - idade
if idade2 <= 9:
    print('De acordo com a sua idade de {} ano(s) , sua categoria é a MIRIM!'.format(idade2))
elif idade2 <=14:
    print('Quem nasceu em {}, tem {} anos de idade.'.format(idade,idade2))
    print('De acordo com a sua idade de {} anos, sua categoria é a INFANTIL!'.format(idade2)) 
elif idade2 <=19:
    print('Quem nasceu em {}, tem {} anos de idade.'.format(idade,idade2))
    print('De acordo com a sua idade de {} anos, sua categoria é a JÚNIOR!'.format(idade2))
elif idade2 <=25:
    print('Quem nasceu em {}, tem {} anos de idade.'.format(idade,idade2))
    print('De acordo com a sua idade de {} anos, sua categoria é a SÊNIOR!'.format(idade2))
else:
    print('Quem nasceu em {}, tem {} anos de idade.'.format(idade,idade2))
    print('De acordo com a sua idade de {} anos, sua categoria é a MASTER!'.format(idade2))