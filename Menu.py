import sys
import time
import socket

from bd import Mongo
from Sensor import Sensor
from Adafruit import Adafruit
from lcd.lcd_ecologic import lcd_ecologic

class Menu:
    def __init__(self):
        self._mongo = Mongo()
        self._sensor = Sensor()
        self._adafruit = Adafruit()
        self._lcd = lcd_ecologic()
    
    def leerSensorTyH(self):
        try:
            self._sensor.lectura()
            self._mongo.insertarDatos(self._sensor.getTemperatura(),self._sensor.getHumedad(), self._sensor.getFecha())
            print('Temperatura={0:0.1f}* Humedad={1:0.1f}%'.format(self._sensor.getTemperatura(), self._sensor.getHumedad()))
            print(self._sensor.getFecha())
        except:
            sys.exit(1)
            
    def publicaDatos(self):
        self._adafruit.publicarHumedad(self._sensor.getHumedad())
        self._adafruit.publicarTemperatura(self._sensor.getTemperatura())
        self._adafruit.publicarHumedadPlanta(30.1)
        
    def imprimeDatos(self):
        self._lcd.imprimirPantalla(self._sensor.getHumedad(), self._sensor.getTemperatura(), 30.0)
    
    def run(self):
        try:
            socket.create_connection(('google.com', 80))
            # Send data to Firebase
        except OSError:
            print("Sin conexion a Internet...")

            while True:
                self.leerSensorTyH()
                self.publicaDatos()
                self.imprimeDatos()
                time.sleep(12)
            else:
                print("Tiempo excedido")