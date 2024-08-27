import calendar

anio = int(input("ingrese el año: "))
mes = int(input("ingrese el mes [1-12]: "))

calend = calendar.TextCalendar(calendar.SUNDAY)

calendario_mes = calend.formatmonth(anio, mes)
print(calendario_mes)