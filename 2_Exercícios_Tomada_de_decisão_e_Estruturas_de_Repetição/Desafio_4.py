print('Vamos avaliar notas de alunos e classifica-los!')
while True:
    nota = int(input("Digite a nota do aluno (de 0 a 10): "))

    if 0 <= nota <= 10:
        print(f"Você informou a nota {nota}.")

        if nota >= 7:
            print(f"O aluno está APROVADO com a nota {nota}.")
        else:
            print(f"O aluno está REPROVADO com a nota {nota}.")
        break

    else:
        print(
            "Valor inválido! Por favor, digite uma nota válida entre 0 e 10.")
