import datetime

hoje = datetime.datetime.now()

print(type(hoje))

print(hoje.day)
print(hoje.month)
print(hoje.year)
print(hoje.hour)
print(hoje.minute)
print(hoje.second)
print(hoje.microsecond)

print(hoje.strftime('%x - %X'))

meu_aniversario = datetime.datetime(2005, 4, 19)

print(f'Eu ja vivi {hoje - meu_aniversario}.')

dias_vividos = hoje - meu_aniversario

dif_tempo = datetime.timedelta(1000)

dia_1000_depois = hoje + dif_tempo

print(dia_1000_depois)