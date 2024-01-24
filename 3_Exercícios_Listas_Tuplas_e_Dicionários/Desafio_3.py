#Crie um dicionário representando um carrinho de compras.
#Adicione produtos (chaves) e quantidades (valores) ao carrinho.
#Calcule o total do carrinho de compra.

carrinho_de_compras = {}


def adicionar_produto(carrinho, produto, quantidade, preco_unitario):
    if produto in carrinho:
        carrinho[produto]["quantidade"] += quantidade
    else:
        carrinho[produto] = {
            "quantidade": quantidade,
            "preco_unitario": preco_unitario}


adicionar_produto(carrinho_de_compras, "Fone de Ouvido", 2, 50.0)
adicionar_produto(carrinho_de_compras, "Carregador veícular", 1, 35.0)
adicionar_produto(carrinho_de_compras, "Bateria recarregável", 3, 55.0)


def calcular_total(carrinho):
    total = 0
    for produto, info in carrinho.items():
        total += info["quantidade"] * info["preco_unitario"]
    return total


total_do_carrinho = calcular_total(carrinho_de_compras)

print("Carrinho de Compras:")
for produto, info in carrinho_de_compras.items():
    print(f"{produto}: {info['quantidade']} x R${info['preco_unitario']:.2f}")

print(f"\nTotal do Carrinho: R${total_do_carrinho:.2f}")
