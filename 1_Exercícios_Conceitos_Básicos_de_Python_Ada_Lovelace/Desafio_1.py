# Faça um programa que peça dois numeros,
# realize as principais operações soma, 
# Subtração, multiplicação, divisão

from datetime import date

print('Olá, Bem Vindo(a) aos desafios da Squad Ada Lovelace \U0001F603')

print('Eu sou Ada Lovelace e irei lhe acompanhar nesses desafios \U0001F609')

#1
print('Primeiro começamos com as principais operações matematicas')

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
print(f'A Soma dos números digitados é {soma:.2f}')
print(f'A Subtração dos números digitados é {subtracao:.2f}')
print(f'A Multiplicação dos números digitados é {multiplicacao:.2f}')
print(f'A Divisão dos números digitados é {divisao:.2f}')

#2
print('Estamos só aquecendo! \U0001F609')

nascimento = int(input('Agora me informe o seu ano de nascimento: '))
hoje = date.today().year
idade = hoje - nascimento
print(f'Sua idade atual é  {idade}')

#3
print('Legal né? Agora vamos calcular medidas de comprimento!')

quilometro = float(input('Me diga uma quantidade de quilômetros para eu transformar em metros, centímetros e milímetros: '))

metros = (quilometro*1000)
centimento = (quilometro*100000)
milimetros = (quilometro*1000000)

print('E aqui está seu resultado!')
print(f'Seu valor em metros é {metros:.2f} m')
print(f'Seu valor em centímetros é {centimento:.2f} cm')
print(f'Seu valor em milímetros é {milimetros:.2f} mm')

#4
print('Estou indo bem né? Agora vamos calcular seu consumo médio de combustível!')

litros = float(input('Me fale uma quantidade de litros que tem consumido: '))
distancia = float(input('E a distancia que você tem percorrido em quilometros: '))
consumo_medio = distancia/litros

print(f'Seu consumo médio é {consumo_medio:.2f} km/l')

#5
print('Agora vamos falar de dinheiro! Me diga seu salario bruto e eu calculo para você seu salario liquido e o imposto que você vai pagar (infelizmente)!')

salario_bruto = float(input('Me diga seu salario bruto: '))

# Cálculo da alíquota do imposto de renda
aliquota = 0
aliquota += (salario_bruto > 1903.98) * (salario_bruto <= 2826.65) * 0.075
aliquota += (salario_bruto > 2826.65) * (salario_bruto <= 3751.05) * 0.15
aliquota += (salario_bruto > 3751.05) * (salario_bruto <= 4664.68) * 0.225
aliquota += (salario_bruto > 4664.68) * 0.275

imposto = salario_bruto * aliquota
salario_liquido = salario_bruto - imposto

print(f"O seu salário líquido fica em R$ {salario_liquido:.2f} e o Imposto de Renda é de R$ {imposto:.2f} à uma aliquota de {aliquota*100}%") 

#6
print('Vamos mudar desse assunto triste de salario né!')

print('Olha que legal, você está querendo viajar?!')

distancia = float(input('Me diga qual a distância em quilometros da sua viagem: '))

velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

# Calcular o tempo de viagem em horas
tempo_aviao = distancia / velocidade_aviao
tempo_carro = distancia / velocidade_carro
tempo_onibus = distancia / velocidade_onibus

print(f"Seu tempo de viagem para a distância de {distancia} km:")
print(f"De Avião: {tempo_aviao:.2f} horas")
print(f"De Carro: {tempo_carro:.2f} horas")
print(f"De Ônibus: {tempo_onibus:.2f} horas")

#7
print('Vamos falar da sua saúde agora, assunto muito importante!')

altura = float(input('Por favor, me diga sua Altura em metros: '))
peso = float(input('E agora, me diga seu Peso em kg: '))

# calculo de IMC
imc = peso/(altura*altura)
print(f"Seu Índice de Massa Corporal (IMC) é : {imc:.2f}")

classificacao = "Você está obeso." * (imc >= 30) + \
  "Você está com sobrepeso." * (25 <= imc < 30) + \
  "Você está com peso normal." * (18.5 <= imc < 25) + \
  "Você está abaixo do peso." * (imc < 18.5)
print(classificacao)

#8
print('Já vimos muitas coisas até agora, né! E eu estou adorando conhecer você um pouco mais.')
print('Vamos calcular seu salário total?')

ganho_hora = float(input("Me diga quanto você ganha por hora trabalhada? "))
horas_trabalhadas = float(input("E também quantas horas por mês você trabalha? "))

salario_total = ganho_hora * horas_trabalhadas

print(f"Cheguei a conclusão que seu  salário total neste mês é de: R${salario_total:.2f}")

#9
print('Estamos chegando ao final do nosso desafio, até agora você gostou?')
print('Voltando a falar sobre saúde.')

horas_exercicio = float(input("Me diga quantas horas de exercício físico você faz por semana (seja sincero rsrs): "))
minutos_exercicio = horas_exercicio * 60
calorias_por_semana = minutos_exercicio * 5
# Calcular o total de calorias queimadas em um mês (considerando 4 semanas em um mês)
calorias_por_mes = calorias_por_semana * 4
# Imprimir o total de calorias queimadas em um mês

print('Pensando que se gaste 5 calorias por minuto de exercício:')
print(f"Seu total de calorias queimadas em um mês é de: {calorias_por_mes:.2f}")

#10
print('Estamos conversando faz tempo, e eu estou muito feliz em ti conhecer melhor!')
print('Agora para fechar com chave de ouro, posso fazer algumas últimas perguntas?')

nome = str(input('Qual seu nome completo? '))
cidade = str(input('Em qual cidade você mora? '))
profissao = str(input('Qual a sua profissão? '))
hobby = str(input('E me fale um hobby que você mais gosta? '))

mensagem = print(f"Vamos revisar então se eu entendi bem! Seu nome é {nome}, muito prazer! \
Já sei que sua idade é {idade} anos e que mora em {cidade}. É incrível que você trabalhe como {profissao}\
 e goste de {hobby}, isso é muito interessante!")

print('Obrigada por compartilhar comigo um pouco da sua vida, eu adorei ti conhecer. \U0001F609 \U0001F603')
