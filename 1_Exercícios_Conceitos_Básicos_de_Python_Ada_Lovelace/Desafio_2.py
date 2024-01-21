from datetime import date, datetime
data_nasc = input("infomme a data de nascimento (dd/mm/yyyy): ")
##data_nasc = "05/05/1987"
data_formatada = datetime.strptime(data_nasc, '%d/%m/%Y')
data_atual = date.today()
Idade_atual = data_atual.year - data_formatada.date().year - ((data_atual.month, data_atual.day) < (data_formatada.month, data_formatada.day))
print(f"Data nascimento: {data_nasc} \nData agora: {date.strftime(data_atual,'%d/%m/%Y') } \nIdade: {Idade_atual}" )

