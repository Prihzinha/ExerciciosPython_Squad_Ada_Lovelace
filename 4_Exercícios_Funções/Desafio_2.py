#Reverso do número. Faça uma função que retorne o reverso de um
#número inteiro informado. Por exemplo: 127 -> 721.

def reverse(a):
    numreverso = a[::-1]
    return numreverso
numero = input("Digite um numero? ")
print(f'O numero intertido fica assim: {reverse(numero)}')