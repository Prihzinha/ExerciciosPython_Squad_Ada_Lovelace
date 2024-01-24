#Crie um programa que leia quanto dinheiro uma pessoa tem na
#carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
#Considere a tabela de conversão abaixo:
#Dólar Americano: R$ 4,91
#Peso Argentino: R$ 0,02
#Dólar Australiano: R$ 3,18
#Dólar Canadense: R$ 3,64
#Franco Suiço: R$ 0,42
#Euro: R$ 5,36
#Libra esterlina: R$ 6,21

def euro(valor):
    vconvert = valor / 5.36
    return float("{:.2f}".format(vconvert))

def libra(valor):
    vconvert = valor / 6.21
    return float("{:.2f}".format(vconvert))

def dolarAME(valor):
    vconvert = valor / 4.91

    return float("{:.2f}".format(vconvert))

def PesoARG(valor):
    vconvert = valor / 0.02
    return float("{:.2f}".format(vconvert))

def dolarAUS(valor):
    vconvert = valor / 3.18
    return float("{:.2f}".format(vconvert))

def dolarCAN(valor):
    vconvert = valor / 3.64
    return float("{:.2f}".format(vconvert))

def francoSUI(valor):
    vconvert = valor / 0.42
    return float("{:.2f}".format(vconvert))

val = float(input("Valores em reais para conversão: R$"))

print (f"Valores Convertidos:\nDolar Americano: ${dolarAME(val)}\nPeso Argentino: ${PesoARG(val)}\nDolar Australiano: ${dolarAUS(val)}\nDolar Canadense: $ {dolarCAN(val)}\nFranco Suiço: ${francoSUI(val)}\nEuro: ${euro(val)}\nLibra Esterlina {libra(val)}")