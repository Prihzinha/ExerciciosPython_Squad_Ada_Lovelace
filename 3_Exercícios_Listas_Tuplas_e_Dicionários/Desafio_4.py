#Crie um dicionário representando contatos (nome, telefone).
#Permita ao usuário procurar por um contato pelo nome.

contato = {'Joao': "(99) 99999-9999", 'Maria': "(88) 88888.8888", 'Jose': "(77) 77777.7777", 'Cida': "(66) 66666.6666"}
procurar = input ("Digite o nome: ")
for chave, valor in contato.items():
    if chave.upper() == procurar.upper():
        print(f"{chave} localizado. Número Telefone {valor}")
        break
    else:
        print(f"{procurar} não localizado")
