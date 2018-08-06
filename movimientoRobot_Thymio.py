import dbus
import dbus.mainloop.glib
import gobject
from optparse import OptionParser
import network as net
import os
import time
from datetime import time as dtTime
from datetime import datetime
from datetime import timedelta

class MovimientoRobot:
	
	def __init__(self):

		self.network = net.initNetwork()

		os.system("asebamedulla \"ser:device=/dev/ttyACM0\" &")
		time.sleep(2) #Da tiempo al S.O. a ejecutar la orden anterior

		self.velDerCalibrada = 243
		self.velIzqCalibrada = 245
		self.velGiro = 100


	def mueve(self,velDer,velIzq):
		self.network.SetVariable("thymio-II", "motor.left.target", [velIzq])
		self.network.SetVariable("thymio-II", "motor.right.target", [velDer])
		

	def muevePorUnTiempo(self,tiempoDeMovimiento, velDer, velIzq):
		""" Mueve el robot por un tiempo determinado a unas 
		velocidades que pueden ir de -500 a 500, pasando por 0 (parado) """
		
		self.mueve(velDer,velIzq)
		time.sleep(tiempoDeMovimiento)
		self.mueve(0,0)
		
		return True
		
	def pararRobot(self):
		""" Detiene al robot"""
		self.muevePorUnTiempo(100000000, 0, 0)
		return True
		
	def avance(self, segundos,velRuedaDer, velRuedaIzq):
		"""El robot avanza los segundos marcados a una velocidad que puede variar 
		desde -500 (todo atras)  a 500 (todo adelante) pasando por 0 (parada)"""
		self.muevePorUnTiempo(segundos, velRuedaDer, velRuedaIzq)
	
	def atras(self, segundos,velRuedaDer, velRuedaIzq):
		"""El robot avanza los segundos marcados a una velocidad que puede variar 
		desde -500 (todo atras)  a 500 (todo adelante) pasando por 0 (parada)"""
		self.muevePorUnTiempo(segundos, -1*velRuedaDer, -1*velRuedaIzq)
		
	def giroDer(self, segundos,velRuedaDer, velRuedaIzq):
		"""El robot gira los segundos marcados a una velocidad que puede variar 
		desde -500 (todo atras)  a 500 (todo adelante) pasando por 0 (parada)"""
		self.muevePorUnTiempo(segundos, -1*velRuedaDer,velRuedaIzq)
		
	def giroIzq(self, segundos,velRuedaDer, velRuedaIzq):
		"""El robot gira los segundos marcados a una velocidad que puede variar 
		desde -500 (todo atras)  a 500 (todo adelante) pasando por 0 (parada)"""
		self.muevePorUnTiempo(segundos, velRuedaDer,-1*velRuedaIzq)
		


 
if __name__ == '__main__':
    
    robot = MovimientoRobot()
    robot.giroDer(1, 100, 100)
    
    
    
   
