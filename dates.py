## This is the first lesson of intermediate python course of Mouredev

#Importaciones 
from datetime import datetime, timedelta
from datetime import date 
from datetime import time

#1. Crea una variable con la fecha y hora actual.

actual_date = datetime.now()
print(actual_date)
#2. Imprime solo el año, mes y día de la fecha actual.
print(f"The date of today is {actual_date.day} / {actual_date.month} / {actual_date.year } ")
#3. Crea una fecha específica: 25 de diciembre de 2025 y muéstrala.

specific_date =  date(2025,12,25)
print(specific_date)
#4. Muestra solo la hora, los minutos y los segundos de un objeto time.

tiempo = time(6,25,39)
print(f"Son las {tiempo.hour} y {tiempo.minute} minutos , {tiempo.second} segundos")

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.
enero = date(2026,1,1)
esto_is_hoy = date.today()
diferencia_between =  enero - esto_is_hoy
print(f"Left time for new year : {diferencia_between}")
#6. Crea una función que reciba una fecha y devuelva su timestamp.

def get_timestamp(date):
    return date.timestamp()

print(get_timestamp(datetime.now()))
    
       
#7. Suma 30 días a la fecha actual usando timedelta.
def sumar_fecha ():
    ahora = datetime.now()
    operacion = timedelta(days=30) + ahora
    return operacion
print(sumar_fecha())

#8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 días como simplificación).
mas_un_mes = datetime(2025,9,18) + timedelta(days=30)
print(mas_un_mes)
#9. Compara dos fechas y muestra cuál es anterior.
def date_comparation(d1,d2):
   
    if d1 > d2 :
        print(f"This date {d1} is more current than {d2}")
    elif d2 > d1 :
        print(f"The {d2} is more current than {d1}")
    else :
        print("Dates are equal")
date1 = date(2025,5,1)
date2 = date(2025,1,1)
print(date_comparation(date1,date2))

#10. Crea una lista con varias fechas y ordénalas cronológicamente.

varias_Fechas = [(2025,1,2),(2024,1,2),(2023,1,2),(2022,1,2)]
varias_Fechas.sort()
print(varias_Fechas)

 
