print('Vamos avaliar notas e realizar comparações com possíveis valores inválidos:')

while True:
    nota = int(input("Digite uma nota entre 0 e 10: "))

    if 0 <= nota <= 10:
        print(f"Você informou a nota {nota}.")
        break
    else:
        print(
            "Valor inválido!"
            "Por favor, digite uma nota válida entre 0 e 10."
            )
