
#Faça um Programa que peça as quatro notas de 5 alunos, calcule
#e armazene numa lista a média de cada aluno, imprima o número
#de alunos com média maior ou igual a 7.0.


notasalunos = []
qtdaluno = 0
x = 0
while x < 5:
    linha  = input (f"5 Notas do Aluno {x+1} Separado por espaço: ")
    for i in linha.split():
        notasalunos.append(int(i))

    soma = sum(notasalunos) 
    mediaaluno = soma / len(notasalunos)
    if mediaaluno >= 7: 
        qtdaluno +=1
    x+=1

if qtdaluno == 0:
    print("Nenhum Aluno passou de ano")
elif qtdaluno == 1:
    print("Apenas 1 aluno passou de ano")
elif qtdaluno > 1:
    print(f"{qtdaluno} alunos passaram de ano")
