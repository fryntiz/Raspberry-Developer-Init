#!/usr/bin/python
# -*- encoding: utf-8 -*-

#Importamos Librerías
import RPi.GPIO as GPIO #Librerías GPIO
import time #Importamos la libreria time
import os #Importamos la libreria para comandos de la consola/shell
import random #crea números aleatorios

#Variables
tiempoensegundos = 8
sleep = time.sleep

#Ahora definimos Todos los pines del 2-27 como salida
def MarcarSalida():
    contador = 2 #Contador de GPIO
    GPIO.setmode(GPIO.BCM) #Definimos el modo BCM
    GPIO.setwarnings(False) #Desactivo Errores
    while contador <= 27:
        GPIO.setup(contador, GPIO.OUT)
        contador =  contador + 1

def TodoEncendido():
    contador1 = 2 #contador de GPIO
    while contador1 <= 27:
        GPIO.output(contador1, GPIO.HIGH)
        contador1 =  contador1 + 1

def TodoApagado():
    contador2 = 2 #contador de GPIO
    while contador2 <= 27:
        GPIO.output(contador2, GPIO.LOW)
        contador2 =  contador2 + 1

def seleccionarGPIOaEncender():
    GPIO.setmode(GPIO.BCM) #Definimos el modo BCM
    GPIO.setwarnings(False) #Desactivo Errores
    while True:
        print """
    Escribe el número de GPIO según BCM que quieras encender
        Recuerda que solo funcionan valores desde el 2 al 27

Número elegido:
            """
        seleccionGPIO=input("-->")
        if seleccionGPIO <=27 & seleccionGPIO >= 2:
            GPIO.setup(seleccionGPIO, GPIO.OUT)
            GPIO.output(seleccionGPIO, GPIO.HIGH)
            break
        else:
            print """

                                Esta opción es incorrecta, selecciona un número del 2 al 27

                        """

def seleccionarGPIOaApagar():
    GPIO.setmode(GPIO.BCM) #Definimos el modo BCM
    GPIO.setwarnings(False) #Desactivo Errores
    while True:
        print """
            Escribe el número de GPIO según BCM que quieras apagar
                    Recuerda que solo funcionan valores desde el 2 al 27

            Número elegido:
            """
        seleccionGPIO=int(input("-->"))
        if seleccionGPIO <=27 and seleccionGPIO >= 2:
            GPIO.setup(seleccionGPIO, GPIO.OUT)
            GPIO.output(seleccionGPIO, GPIO.LOW)
            break
        else:
            print """

                                Esta opción es incorrecta, selecciona un número del 2 al 27

                        """

def aleatorio():
    while True:
        GPIOaleatorio = random.randrange(2,27)
        GPIOaleatorio1 = random.randrange(2,27)
        GPIOaleatorio2 = random.randrange(2,27)
        GPIOaleatorio3 = random.randrange(2,27)
        GPIOaleatorio4 = random.randrange(2,27)
        GPIOaleatorio5 = random.randrange(2,27)
        GPIOaleatorio6 = random.randrange(2,27)

        if (GPIO.input(GPIOaleatorio) == GPIO.HIGH):
            GPIO.output(GPIOaleatorio, GPIO.LOW)
        else:
            GPIO.output(GPIOaleatorio, GPIO.HIGH)

        if (GPIO.input(GPIOaleatorio1) == GPIO.HIGH):
            GPIO.output(GPIOaleatorio1, GPIO.LOW)
        else:
            GPIO.output(GPIOaleatorio1, GPIO.HIGH)

        if (GPIO.input(GPIOaleatorio2) == GPIO.HIGH):
            GPIO.output(GPIOaleatorio2, GPIO.LOW)
        else:
            GPIO.output(GPIOaleatorio2, GPIO.HIGH)

        if (GPIO.input(GPIOaleatorio3) == GPIO.HIGH):
            GPIO.output(GPIOaleatorio3, GPIO.LOW)
        else:
            GPIO.output(GPIOaleatorio3, GPIO.HIGH)

        if (GPIO.input(GPIOaleatorio4) == GPIO.HIGH):
            GPIO.output(GPIOaleatorio4, GPIO.LOW)
        else:
            GPIO.output(GPIOaleatorio4, GPIO.HIGH)

        if (GPIO.input(GPIOaleatorio5) == GPIO.HIGH):
            GPIO.output(GPIOaleatorio5, GPIO.LOW)
        else:
            GPIO.output(GPIOaleatorio5, GPIO.HIGH)

        if (GPIO.input(GPIOaleatorio6) == GPIO.HIGH):
            GPIO.output(GPIOaleatorio6, GPIO.LOW)
        else:
            GPIO.output(GPIOaleatorio6, GPIO.HIGH)

        sleep(0.4)

def limpiar():
    GPIO.cleanup()

# ------------------------CONTROL DE ENTRADA PARA EL MENÚ-----------------------
while True:
    print """
Este menú controla principalmente los pines GPIO del 2 al 11 según BCM
Recuerda que la tensión de salida es de 3,3V

Elige una opción:

1 Poner todos como OUT/SALIDA
2 Encender todos los GPIO 2-27
3 Apagar todos los GPIO 2-27
4 Seleccionar GPIO para activar  >X (no funciona)
5 Seleccionar GPIO para apagar   >X (no funciona)
6 Aleatorios encendidos y apagadados
7 Limpiar
8 Salir
"""

    opcion=input("-->")
    if opcion == 1:
        MarcarSalida()

    elif opcion == 2:
        MarcarSalida()
        TodoEncendido()

    elif opcion == 3:
        MarcarSalida()
        TodoApagado()

    elif opcion == 4:
        seleccionarGPIOaEncender()

    elif opcion == 5:
        seleccionarGPIOaApagar()

    elif opcion == 6:
        MarcarSalida()
        aleatorio()

    elif opcion == 7:
        limpiar()

    elif opcion == 8:
        break
    else:
        print "Esta opción es incorrecta, selecciona un número del 1 al 4"
