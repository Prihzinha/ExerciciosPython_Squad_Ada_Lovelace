#Escreva um script que pergunta ao usuário se ele deseja converter
#uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
#cada opção, crie uma função.

def ConvertCelsius (vFahrenheit):
    vcelsius = vFahrenheit-32
    return vcelsius

def ConvertFahrenheit (vcelsius):
    vFahrenheit = 32 - vcelsius
    return vFahrenheit

def menu(Escolha):
    if tp == "F":
        return (f'A temperatura {grau}°F é {ConvertCelsius(grau)}°C')
    elif tp == "C":
        return (f'A temperatura {grau}°C é {ConvertFahrenheit(grau)}°F')
    else:
        return ("Escolha C ou F")    
tp = input("Escolha 'C' Celsius > Fahrenheit ou 'F' Fahrenheit > Celsius: ").upper()
grau = float(input("Informe a temperatura de Conversão: "))
             
print(menu(tp))