n1 = input('Digite algo: ')
print("O tipo primitivo do valor digitado é: ", type (n1))
print('O que foi digitado só tem espaços', n1.isspace())
print('É um número?', n1.isnumeric())
print('É alfabetico?', n1.isalpha())
print('É alfanumérico?', n1.isalnum())
print('Está em letra maiúscula?', n1.isupper())
print('Está em letra minúscula?', n1.islower())
print('Está capitalizado', n1.istitle())