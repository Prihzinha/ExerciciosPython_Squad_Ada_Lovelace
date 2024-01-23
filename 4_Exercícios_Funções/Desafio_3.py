#Escreva um script que pergunta ao usuário se ele deseja converter
#uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
#cada opção, crie uma função.

def ConvertCelsius (vFahrenheit):
    vcelsius = vFahrenheit-32
    return vcelsius

def ConvertFahrenheit (vcelsius):
    vFahrenheit = 32 - vcelsius
    return vFahrenheit

tp = input("Escolha 'C' Celsius > Fahrenheit ou 'F' Fahrenheit > Celsius: ").upper()
grau = float(input("Informe a temperatura de Conversão: "))
             
if tp == "F":
    print(f'A temperatura {grau}°F é {ConvertCelsius(grau)}°C')
elif tp == "C":
    print(f'A temperatura {grau}°C é {ConvertFahrenheit(grau)}°F')
else:
    print("Escolha C ou F")