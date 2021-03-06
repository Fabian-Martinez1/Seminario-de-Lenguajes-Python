import csv
import os

def paises(csv_reader:list[list[str]]):
    for linea in csv_reader:
        if linea[1] == "TV Show" and "Argentina" in linea[5]: 
            print(f"{linea[2]:<40} {linea[3]}")

def todos_paises(csv_reader:list[list[str]]):
    for linea in csv_reader:
        if linea[1] == "TV Show" and "Argentina" in linea[5]: 
            print(f"{linea[2]:<40} {linea[3]}")
            
ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "Practica3", "netflix_titles.csv")

archivo = open(ruta_archivo, "r", encoding="utf-8")
csv_reader = csv.reader(archivo, delimiter=',')

#encabezado = csv_reader.__next__()
encabezado = next(csv_reader)
datos = list(csv_reader)
print(encabezado)
paises(datos)
todos_paises(datos)
archivo.close()