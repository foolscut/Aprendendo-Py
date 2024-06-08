'''try:
   a = int(input('Digite um número: '))
   b = int(input('Digite outro número: '))
   c = a/b
except (ValueError, TypeError):
   print(f'Erro com o tipos de dados digitados')
except ZeroDivisionError:
   print('Erro de divisão por zero, nada se divide por 0')
except KeyboardInterrupt:
   print('O usuário preferiu não informar os dados, ou apertou enter sem digitar nada antes')
except Exception as error:
   print(f'O erro encontrado foi {error.__cause__}')
else:
   print(f'A divisão de {a} / {b} é =  {c:.1f}')
finally:
   print('Volta logo, cuzão')'''


'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

      
from ex113 import leiaInt, leiafloat
num = leiaInt('Digite um número inteiro:  ')
num2 = leiafloat('Digite um número REAL: ')
print(f'O valor inteiro digitado foi {num} e o real foi {num2}')
