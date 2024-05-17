import time                        #Importamos la Librería de Acceso de Tiempo y Conversiones.
import os                          #Importamos la Librería de Interfaces misceláneas del Sistema Operativo.
import math                        #Importamos la Librería de Funciones Matemáticas.

def espacio(x):                    
    if x >= 1:
        print('')
        x = x-1

wait = time.sleep                  #Esta función permite detener el proyecto durante un tiempo y luego permitir que continúe sin alteraciones
blank = os.system('cls')

while True:                                                 #Es un ucle que ejecuta un bloque de código mientras la condición sea "True".
    print('''Selección de operación que desea realizar:     #Imprimir las operación que se desea realizar.
    1) Calcular Seno                                        #Esta es la Opción para Calcular el Seno.
    2) Calcular Coseno                                      #Esta es la Opción para Calcular el Coseno.
    3) Calcular Tangente                                    #Esta es la Opción para Calcular el Tangente.
    4) Apagar Calculadora''')                               #Esta es la Opción de Salir de la Calculadora.
    espacio(1)
          
    c = float(input())                             #Representación de un Número Positivo o Negativo con Decimales.
    
    if c == 4:                                     #Ejecutar la opción 4) Apagar Calculadora.
        print('Gracias por usar esta calculadora. Creada por: Luigi Delgado')           #Imprimir mensaje de apagado de la calculadora.
        wait(2)
        quit()
    
    if c == 1:                                      #Ejecutar la Opción 1) Calcular Seno.
        a = float(input("Escriba el número: "))     #Escribir el Número a Calcular
        res = math.sin(a)                           #Aquí está la Función de la Seno.
        espacio(2)
        print('El resultado es:', res)              #Imprimir Resultado del Seno.
        continue

    if c == 2:                                      #Ejecutar la Opción 2) Calcular Coseno.
        a = float(input("Escriba el número: "))     #Escribir el Número a Calcular
        res = math.cos(a)                           #Aquí está la Función del Coseno.
        espacio(2)
        print('El resultado es:', res)              #Imprimir Resultado del Coseno.
        continue

    if c == 3:                                      #Ejecutar la Opción 3) Calcular Tangente.
        a = float(input("Escriba el número: "))     #Escribir el Número a Calcular
        res = math.tan(a)                           #Aquí está la Función de la Tangente.
        espacio(2)
        print('El resultado es:', res)              #Imprimir Resultado del Tangente.
        continue