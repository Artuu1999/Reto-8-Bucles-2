## Reto #8 Bucles 2
Espero que se encuentren excelente estimados lectores, en el presente repositorio haremos varios ejemplos de código en Python utilizando lo aprendido acerca de los bucles dentro de nuestra clase de programación de computadores.

## Ejemplo No. 1
Realizar un programa que imprima un listado de los número del 1 al 100 con su respectivo número cuadrado.
```sh
x : int = 0 #Se inicializa en 0
for x in range(1, 101): #Determinamos el rango del ciclo, en este caso del 1 al 101, ya que el programa toma en cuenta un valor menos del número que cierra el intervalo
    print("El cuadrado del número "+str(x)+", es "+str(x**2)+"") #Imprimimos el número y es cuadrado de dicho número
    x += 1 # Actualizamos el ciclo
```
## Ejemplo No. 2
Diseñar un programa, el cual al ejecutarse imprima una lista de números pares dentro del rango del 2 al 1000, posteriormente que imprima una lista de número impares dentro del rango de 1 al 999.
```sh
p : int = 2 #Inicializamos la variable de números pares
for p in range (1, 1001): #Determinamos el rango
    if p % 2 == 0: #Condicionamos para que el ciclo imprima los números que al dividirlos en 2 su residuo sea 0
     print(p) #Imprimimos la lista de números pares
     
i : int = 2 #Inicializamos la variable de números impares
for i in range (1, 1001):  #Determinamos el rango
    if i % 2 != 0: #Condicionamos para que el ciclo imprima los números que al dividirlos en 2 su residuo sea diferente a 0
     print(i) #Imprimimos la lista de números impares
```
## Ejemplo No. 3
Realizar un programa que imprima los números pares descendentes hasta 2
```sh
n = int(input("Ingrese numero natural: ")) #Solicitar el ingreso de la variable
for n in range (n, 2, -2): #Ingresar el rango mediante el ciclo for
  if n%2 == 0: #Condicionar el resultado
     print(n) #Imprimirlo
  else: #En caso que no se cumpla
     print (n-1) #Imprimir el mismo resultado pero restando 1
```
## Ejemplo No. 4
Diseñar un código, el cual al correrlo imprima los números hasta determinado número, con su respectivo número factorial
```sh
x : int = 1 #Inicializar la lista
n = int(input("Ingrese número: ")) #Ingresar el fin del rango
for y in range (1, n+1): #Indicar el rango de la lista
    x *= y #Actualizar las variables
print ("El factorial del número "+str(n)+" es "+str(x)+"") #Imprimir el listado finalmente

```
## Ejemplo No. 5
Crear un programa que al indicar un número, imprima el resultado de elevar 2 a la aquel número ingresado
```sh
x : int = 1 #Inicializar la variable
n = int(input("Ingrese numero natural: ")) #Solicitar el ingreso de la potencia
for y in range (n): #Declarar el rango mediante el ciclo for
    x *= 2 #Actualizar la variable
print ("El resultado de 2 elevado a la "+str(n)+" es "+str(2**n)+"") #Imprimir el resultado
```
## Ejemplo No. 6
Ingresar un número natural x y elevarlo a la potencia de otro número natural ingresado
```sh
x = int(input("Ingrese numero natural: ")) #Solicitar el ingreso de la base
n = int(input("Ingrese numero natural: ")) #Solicitar el ingreso del exponenete
potencia = 1 #Inicialzar el ciclo
for y in range (n): #Determinar el rango
    potencia *= x #Actualizar el ciclo
print("El resultado de "+str(x)+" elevado a la "+str(n)+" es "+str(x**n)+"") #Imprimir el resultado
```
## Ejemplo No. 7
Mediante el uso de ciclos for, imprimir la tabla del 9
```sh
x : int = 1 #Inicializar la tabla
n = int(input("Hasta que número deseas la tabla: ")) #Solicitar el ingreso del rango
for y in range (0, n-1, 9): #Ingresar el rango y determinar que aumente de 9 en 9
    print (y) #Imprimir la tabla de multiplicar
```
## Ejemplo No. 8
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Usando math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$
```sh
import math #Importar la función matemática

def exponente(x:int): #Definir la función
    return math.exp(x) #Retornar la función exponencial aplicada en x
def aproximacion(x:int, i:int): 
    aproximacion = 0 #Inicializar
    for n in range(n+1): #Declarar el rango dentro del ciclo for
        aprox += (x**i)/math.factorial(i) #Realizar la operación para encontrar el valor aproximado
    
if __name__ == "__main__": #Retornar la función
    x = int(input("Ingrese la variable x: ")) #Ingresar la variable en x
    i = int(input("Ingrese las veces: "))  #Ingresar las veces que se quiere repetir el ciclo
    exponente = exponente(x)
    print("El resultado de usando la función exponencial de math es "+str(exponente)+"") #Imprimir el valor real
    aproximacion = aproximacion(x, i)
    print("El resultado usando la serie de Maclaurin es "+str(aproximacion)+"") #Imprimir el valor aproximado
```
## Ejemplo No. 9
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Usando math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

```sh
import math #Importar la función matemática
def seno(x:float, n:int) -> float: #Definir la función
    real = math.sin(x) #Retornar la función seno aplicada en x
    aproximacion = 0 #Inicializar
    for i in range(n+1): #Declarar el rango dentro del ciclo for
        aprox += ((-1)**i) * ((x**(2*i+1)) / (math.factorial(2*i+1))) #Realizar la operación para encontrar el valor aproximado
    diferancia = real - aproximacion #Restar el valor real y el aproximado
    
if __name__ == "__main__": #Retornar la función
    x = float(input("Ingrese un numero: ")) #Ingresar la variable en x
    n = int(input("Ingrese la cantidad de veces: ")) #Ingresar las veces que se quiere repetir el ciclo
    print("El resultado usando la serie de Maclaurin es "+str(aproximacion)+"") #Imprimir el valor aproximado
    print("El resultado usando la función math "+str(real)+"") #Imprimir el valor real
    print("La diferencia entre el valor aproximado y real es "+str(diferencia)+"") #Imprimir el valor de la diferencia
```
## Ejemplo No. 10
Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Usando math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

```sh
import math #Importar la función matemática
def cotangente(x:float, n:int) -> float: #Definir la función
    real = math.atan(x) #Retornar la función cotangente aplicada en x
    aproximacion = 0 #Inicializar
    for i in range(n+1): #Declarar el rango dentro del ciclo for
        aprox += ((-1)**i) * ((x**(2*i+1)) / (math.factorial(2*i+1))) #Realizar la operación para encontrar el valor aproximado
    diferancia = real - aproximacion #Restar el valor real y el aproximado
    
if __name__ == "__main__": #Retornar la función
    x = float(input("Ingrese un numero: ")) #Ingresar la variable en x
    n = int(input("Ingrese la cantidad de veces: ")) #Ingresar las veces que se quiere repetir el ciclo
    print("El resultado usando la serie de Maclaurin es "+str(aproximacion)+"") #Imprimir el valor aproximado
    print("El resultado usando la función math "+str(real)+"") #Imprimir el valor real
    print("La diferencia entre el valor aproximado y real es "+str(diferencia)+"") #Imprimir el valor de la diferencia
```
## FIN
Hasta acá llega nuestro camino en el presente repo, espero que haya sido de tu interés, si encuentras algún error o alguna inconsistencia, no dudes en contactarme y hacermela saber.
Muchas Gracias por tu atención.

   **"A cada instante se pone a cero el contador y el ser humano tiene un don maravilloso: la oportunidad de empezar, e intentarlo de nuevo.r"**
         - Arturo Pérez Reverte
