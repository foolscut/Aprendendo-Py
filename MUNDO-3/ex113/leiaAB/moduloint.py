def leiaInt(msg):
   while True:
      try:
         n1 = int(input(msg))
      except (ValueError, TypeError):
         print('\033[31mERRO! O Valor digitado não é um número inteiro!\033[m')
      except (KeyboardInterrupt):
         print('\33[31mO usuário interrompeu a aplicação\033[m')
         return 0
      else:
         return n1
      
def leiafloat(msg):
   while True:
      try:
         n2 = float(input(msg))
      except (TypeError, ValueError):
         print('\033[31mERRO! O Valor digitado não é um número REAL!\033[m ')
      except (KeyboardInterrupt):
         print('\33[31mO usuário interrompeu a aplicação\033[m')
         return 0
      else:
         return n2
