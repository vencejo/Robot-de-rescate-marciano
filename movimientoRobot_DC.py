# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
import pi2go, time
import sys
import tty
import termios
from datetime import time as dtTime
from datetime import datetime
from datetime import timedelta

class MovimientoRobot:
	
	def __init__(self):
		pi2go.init()
		self.velDerCalibrada = 49			# valores -100 a 100
		self.velIzqCalibrada = 50			# valores -100 a 100

	def mueve(self, velDer,velIzq):
		pi2go.go(velIzq,velDer)
		
	def avance(self, segundos,velRuedaDer, velRuedaIzq):
		self.mueve(self.velDerCalibrada,self.velIzqCalibrada)
		time.sleep(segundos)
		self.mueve(0,0)
	
	def atras(self, segundos,velRuedaDer, velRuedaIzq):
		self.mueve(-1*self.velDerCalibrada, -1*self.velIzqCalibrada)
		time.sleep(segundos)
		self.mueve(0,0)
		
	def giroDer(self, segundos,velRuedaDer, velRuedaIzq):
		self.mueve(-1*self.velDerCalibrada, self.velIzqCalibrada)
		time.sleep(segundos)
		self.mueve(0,0)
		
	def giroIzq(self, segundos,velRuedaDer, velRuedaIzq):
		self.mueve(self.velDerCalibrada, -1*self.velIzqCalibrada)
		time.sleep(segundos)
		self.mueve(0,0)
		


 
if __name__ == '__main__':
    
    robot = MovimientoRobot()
    robot.giroDer(1, 100, 100)

    


		
   


