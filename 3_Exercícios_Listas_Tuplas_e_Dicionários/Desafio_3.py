#Crie um dicionário representando um carrinho de compras.
#Adicione produtos (chaves) e quantidades (valores) ao carrinho.
#Calcule o total do carrinho de compra.

paises = {'Caneta': 1, 'Caderno': 10, 'Lapis': .5, 'Estojo': 15}
for chave, valor in paises.items():
    print(chave + " = R$ " + str(valor))
    soma = float(valor)

print(f"Valor Total= R$ {soma}")