<h1 align="center"> 馃Desafios </h1>

## ```1) Primer Desafio```  [Resoluci贸n](#Desafio_1)

- Queremos ingresar un n煤mero desde teclado e imprimir si el n煤mero es o no par.
- 驴C贸mo ser铆a el pseudoc贸digo de esto?

```
Ingresar un n煤mero desde teclado
SI es par: 
    Mostrar mensaje: "es par"
SINO:
    Mostrar mensaje: "NO es par"
```

## ```2) Segundo Desafio``` [Resoluci贸n](#Desafio_2)

- Queremos ingresar un n煤mero desde el teclado e imprimir si es m煤ltiplo de 2,3 o 5.
- **Pista:** Python tiene otra forma de la sentencia condicional: **if-elif-else**

## ```3) Tercer Desafio``` [Resoluci贸n](#Desafio_3)

- Dado una letra ingresada por el teclado, queremos saber si es may煤scula o min煤scula.

## ```4) Cuarto Desafio``` [Resoluci贸n](#Desafio_4)

- Dado un caracter ingresado por el teclado, queremos saber si es una comilla o no.
- 驴Hay alg煤n problema?

## ```5) Quinto Desafio``` [Resoluci贸n](#Desafio_5)

- Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga m谩s caracteres.

## ```6) Sexto Desafio``` [Resoluci贸n](#Desafio_6)

- Escribir un programa que ingrese desde teclado una cadena de caracteres e imprima cu谩ntas letras ``a`` contiene.

## ```7) Septimo Desafio``` [Resoluci贸n](#Desafio_7)

- Escribir un programa que ingrese 4 palabras desde teclado e imprima aquellas que contienen la letra ```r```.
- **Pensar:** 驴Podemos usar la instrucci贸n **for** tal cual la vimos la clase pasada para las 4 iteraciones?
- La sentencia **for** permite iterar sobre una **secuencia.**

## ```8) Octavo Desafio``` [Resoluci贸n](#Desafio_8)

Vamos a modificar el c贸digo anterior para que imprima la cadena **R** si la palabra contiene la letra r y sino, imprimal ``NO TIENE R``

## ```9) Noveno Desafio``` [Resoluci贸n](#Desadfio_9)

**Ingresar palabras desde teclado hasta ingresar la palabra FIN. Imprimir aquellas que empiecen y terminen con la misma letra**

- 驴Qu茅 estructura de control deberiamos utilizar para realizar esta interaci贸n?驴Podemos utilizar la sentencia for?

## ```10) Decimo Desafio``` [Resoluci贸n](#Desafio_10)

**Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:**

- Cu谩l es el promedio de las notas
- Cu谩ntos estudiantes est谩n por debajo del promedio

驴C贸mo estudiantes est谩n por debajo del promedio?

```
Ingresar las notas
Calcular el promedio
Calcular cu谩ntos tienen notas menores al promedio
```

Obviamente no. **Necesitamos tipos de datos que nos permiten guardar muchos valores**

## ```11)Desafio Onceavo``` [Resoluci贸n](#Desafio_11)

**Necesitamos procesar las notas de los estudiantes de este curso Queremos saber:**

- C煤al es el promedio de las notas
- **Qu茅 estudiantes** est谩n por debajo del promedio

驴Qu茅 diferencia hay con el desafio anterior?

- Deber铆amos ingresar no s贸lo las notas, sino tambi茅n los nombres de los estudiantes.
- 驴Qu茅 soluciones proponen?



Desafio_1
=========
```Py
num = int( input("Ingres谩 un n煤mero: "))
if num % 2 == 0:
    print("Es par")
else:
    print("No es par")
```
Desafio_2
=========
```Py
num = int( input("Ingres谩 un n煤mero: "))
if ((num % 2) == 0):
    print("El nro es multiplo de Dos")
elif((num % 3) == 0):
    print("El nro es multiplo de Tres")
elif((num % 5) == 0):
    print("El nro es multiplo de Cinco")
else:
    print("El nro no es multiplo de 2,3 o 5")
```
Desafio_3
=========

```Py
letra = input("Ingresar una letra: ")
if letra >="a" and letra <="z":
    print("Es min煤scula")
elif letra >= "A" and letra <= "Z":
    print("Es may煤scula")
else:
    print("NO es una letra")
```
Desafio_4
=========

```Py
letra = input("Ingresar un caracter: ")
if letra == "\"":
    print("Es una comilla")
else:
    print("NO es una comilla")
```

Desafio_5
=========

```Py
cadena = input("Ingresar una cadena: ")
cadena2 = input("Ingresar otra cadena: ")
contador_1 = 0
contador_2 = 0
for car in cadena:
    contador_1+=1
for car in cadena2:
    contador_2+=1
if (cadena>cadena2):
    print("La primera cadena es mas grande")
else:
    print("La segunda cadena es mas grande")
```

Desafio_6
=========

```Py
cadena = input("Ingresar una cadena: ")
contador_a = 0
for car in cadena:
    if (car == "a"):
        contador_a+=1
print("La cantidad de letras a es: " , contador_a)
```

Desafio_7
=========
```Py
for i in range(4):
    cadena = input("Ingres谩 una palabra: ")
    if "r" in cadena:
        print(cadena)

#for elem in range(4):
#    cadena = input('Ingresa una cadena: ')
#    encontro = False
#    i=0
#    while(i < len(cadena)) and encontro == False:
#        if cadena[i] == "r":
#            print(cadena)
#            encontro = True
#        i=i+1
```
Desafio_8
=========
```Py
for i in range(4):
    cadena = input("Ingres谩 una palabra: ")
    if "r" in cadena:
        print("TIENE R")
    else:
        print("NO TIENE R")
```

Desafio_9
=========
```Py
cadena = input("Ingres谩 una palabra: ")
while cadena != "FIN":
    if cadena[0] == (cadena[len(cadena)-1]):
        print("Empiezar y terminan con la misma letra")
        print(cadena)
    else:
        print("No empieza y termina con la misma letra")
    cadena = input("Ingres谩 una palabra: ")
```

Desafio_10
```Py
notas = [ 4, 6, 7, 3, 8, 1, 10, 4]
total = 0

for i in range((len(notas))):
    print(notas[i])
    total += notas[i]
promedio = total/(len(notas))
print("El promedio de las notas es: " , promedio)
```

Desafio_11
==========
```Py
notas = {"Janis Joplin":10, "Elvis Presley": 9, "Bob Marley": 5, "Jimi Hendrix": 9}
notas["Bob Marley"]
total = 0


for key in notas:
    print (key, ":", notas[key])
    total += notas[key]

promedio = total/(len(notas))
print("El promedio de las notas es: " , promedio)
debajo_promedio = 0
for i in notas:
    if notas[i] < promedio:
        print("El estudiantes", i , "Esta por debajo del promedio")
        debajo_promedio+=+1

```
