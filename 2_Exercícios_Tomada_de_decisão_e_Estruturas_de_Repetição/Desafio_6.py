login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "admin123":
    print("Acesso permitido. Bem-vindo, admin!")
else:
    print("Erro: Login ou senha incorretos. Acesso negado!")
