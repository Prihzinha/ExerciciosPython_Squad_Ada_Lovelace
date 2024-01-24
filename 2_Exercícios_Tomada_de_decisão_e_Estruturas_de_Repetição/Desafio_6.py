print('Vamos ver como está sua memoria, preciso de seu login e senha para autenticação!')

While True:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == "admin" and senha == "admin123":
       print("Acesso permitido. Bem-vindo, admin!")
       break
    else:
        print("Erro: Login ou senha incorretos. Acesso negado. Tente novamente!")
