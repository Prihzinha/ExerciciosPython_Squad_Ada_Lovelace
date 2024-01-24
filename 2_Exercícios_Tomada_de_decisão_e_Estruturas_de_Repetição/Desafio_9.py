prinf('Digite uma sequência de números, após isso será separados entre pares e impares!')

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro e para encerrar digite 0: ")

    try:
        numero = int(entrada)

        if numero < 0:
            raise ValueError("Erro: Digite apenas números inteiros positivos.")
    except ValueError as e:
        print(e)
        continue

    if numero == 0:
        break

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
