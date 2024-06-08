def metade(n = 0, formato = False):
     res = n/2
     return res if formato is False else moeda(res) 
def dobro(n = 0, formato = False):
    res = n*2
    return res if formato is False else moeda(res)
def aumeta(n = 0,taxa = 0, formato = False):
    res = n + (n*taxa/100)
    return res if formato is False else moeda(res)
def diminui(n = 0,taxa = 0, formato = False):
    res = n - (n * taxa / 100)
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(n = 0,taxa1 = 0,taxa2 = 0):
    print('='*35)
    print('RESUMO DO VALOR'.center(35))
    print('='*35)
    print(f'Preço analisado: \t{moeda(n,)}')
    print('='*35)
    print(f'Metade do preço é: \t{metade(n,True)}')
    print(f'O dobro é: \t\t{dobro(n,True)}')
    print(f'Aumentando {taxa1}% é: \t{aumeta(n,taxa1,True)}')
    print(f'Diminuindo {taxa2}% é: \t{diminui(n,taxa2,True)}')
    print('='*35)