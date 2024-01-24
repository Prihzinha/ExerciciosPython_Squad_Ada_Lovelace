#5. Crie uma função chamada contar_vogais que recebe uma string
#como parâmetro. Implemente a lógica para contar o número de vogais
#na string e retorne o total de vogais. Solicite ao usuário para inserir uma
#frase e utilize a função para contar as vogais.

def contar_vogais(valor):
    valor = valor.upper()
    result = {}
    qtde = 0
    vogais = 'AEIOU'
    for i in vogais:
        if i in valor:
            #result[i] = valor.count(i)
            qtde +=valor.count(i)
    return qtde

frase = input("Insira a frase para contar vogal: ")
print(f"Existem {contar_vogais(frase)} Vogais na Frase '{frase}'")