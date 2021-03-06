import csv
import os
from datetime import date
import datetime 
import calendar
from collections import Counter

def findDay(fecha:str): 
    born = datetime.datetime.strptime(fecha,"%d/%m/%Y %H:%M").weekday() 
    dia = datetime.datetime.strptime(fecha,"%d/%m/%Y %H:%M")
    dia.strftime("%Y/%m/%d")
    print(dia)
    return (calendar.day_name[born]) 

#3/03/2022 07:22

ruta = os.path.dirname(os.path.realpath("."))

path_arch = os.path.join(ruta, "Practica3")
ruta = os.path.join(path_arch, 'BBB_nuevo.csv')

with open(ruta,"r", encoding="utf-8") as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header , logs_recurso = next(data_logs), list(data_logs )

dias_semanales:list[str]

dias_semanales = Counter([findDay(fecha[0]) for fecha in logs_recurso])
print(dias_semanales.most_common(7))

 

