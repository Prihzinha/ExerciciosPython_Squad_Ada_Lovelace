#Crie um dicionário representando contatos (nome, telefone).
#Permita ao usuário procurar por um contato pelo nome.

contato = {"Joao": "(99) 99999-9999", "Maria": "(88) 88888.8888", "Jose": "(77) 77777.7777", "Cida": "(66) 66666.6666"}

def procurar_contato():
    nome = input("Insira o nome do contato: ")
    if nome in contato:
        return contato[nome]
    else:
        return "Contato não encontrado."
    
print(procurar_contato())
