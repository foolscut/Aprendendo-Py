def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31m{entrada} é um Preço Inválido!\033[m')
        else:
            valido = True
            return float(entrada)
