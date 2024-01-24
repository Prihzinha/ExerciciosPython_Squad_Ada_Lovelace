#Faça um programa, com uma função que necessite de três
#argumentos, e que forneça a soma desses três argumentos

def somar(a, b, c):
    resultado = a + b + c
    return resultado

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))
c = int(input("Informe o último número: "))
print(f"A soma é: {somar(a,b,c)}")
    
