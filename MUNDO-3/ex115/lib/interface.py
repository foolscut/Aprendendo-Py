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

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
