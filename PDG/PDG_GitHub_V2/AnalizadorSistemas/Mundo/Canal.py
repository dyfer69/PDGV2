__author__ = 'DiegoFernando'
import os

from xbee import ZigBee

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PDG.settings")
import serial
import django
from AnalizadorSistemas.Mundo import Recolector

django.setup()

Recolector.guardarEntrada(12)

ser = serial.Serial('COM3', 9600)
print(ser)

xbee =ZigBee(ser)
print(xbee)

# Continuously read and print packets
while True:
    try:
        print(1)
        response = xbee.wait_read_frame()

        print(2)
        print(response)
        dataIn = response['status']
        print(dataIn)
        decodificacion = dataIn.decode()


        print(decodificacion)

        contenedor = decodificacion.split(";")




        print(contenedor[0])

        if(contenedor[1]=='A'):
            lola = float(contenedor[0])
            print(lola)
            #Recolector.guardarEntrada(lola)
        else:
            lola = float(contenedor[0])
            print(lola)
            #Recolector.guardarSalida(lola)


    except KeyboardInterrupt:
        break

ser.close()

