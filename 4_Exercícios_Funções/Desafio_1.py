#Faça um programa, com uma função que necessite de três
#argumentos, e que forneça a soma desses três argumentos

def somar(a, b):
    resultado = a + b
    return resultado

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))
print(f"A soma é: {somar(a,b)}")
    