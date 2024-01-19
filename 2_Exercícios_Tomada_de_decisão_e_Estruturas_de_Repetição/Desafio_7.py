idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade inválida. Por favor, digite uma idade positiva.")
elif 0 <= idade <= 12:
    print(f"Você tem {idade} anos, então você é uma CRIANÇA!")
elif 13 <= idade <= 17:
    print(f"Você tem {idade} anos, então você é um ADOLESCENTE!")
elif 18 <= idade <= 59:
    print(f"Você tem {idade} anos, então você é um ADULTO!")
else:
    print(f"Você tem {idade} anos, então vocêé um IDOSO!")
