# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2022, 12))
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
# print(list(enumerate(calendar.day_name)))
#print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])
# print(calendar.monthcalendar(2022, 12))
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day)
