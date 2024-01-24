
#Faça um Programa que peça as quatro notas de 5 alunos, calcule
#e armazene numa lista a média de cada aluno, imprima o número
#de alunos com média maior ou igual a 7.0.


alunos = []

for i in range(5):
    nome_aluno = input(f"Informe o nome do Aluno {i + 1}: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    media_aluno = (nota1 + nota2 + nota3 + nota4) / 4

    alunos.append({"nome": nome_aluno, "media": media_aluno})

alunos_aprovados = sum(1 for aluno in alunos if aluno["media"] >= 7.0)

print("\nMédia dos Alunos:")
for aluno in alunos:
    print(f"{aluno['nome']}: Média {aluno['media']:.2f}")

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
