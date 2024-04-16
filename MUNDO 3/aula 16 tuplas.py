lanche = ('Pao', 'Arroz', 'Feijão', 'Salada', 'Suco', 'Carne')
for comida in range(0, len(lanche)):
    print(f'Preciso comprar {lanche[comida]}')

for comida in lanche:
    print(f'Preciso comprar {comida}')

for pos, comida in enumerate(lanche):
    print(f'Preciso comprar {comida} {pos}')
    print(sorted(lanche))
# count é um contador
# index mostra em qual posição esta oq se procura