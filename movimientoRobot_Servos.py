# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import sys
import Adafruit_PCA9685
import time
from datetime import time as dtTime
from datetime import datetime
from datetime import timedelta

class MovimientoRobot:
	
	def __init__(self):
		# Initialise the PCA9685 using the default address (0x40).
		self.pwm = Adafruit_PCA9685.PCA9685()
		# Set frequency to 60hz, good for servos.
		self.pwm.set_pwm_freq(60)
		self.servo_max=500
		self.servo_min=200

	def parada(self):
		self.pwm.set_pwm(0, 0, 301)
		self.pwm.set_pwm(1, 0, 301)
		
	def avance(self, segundos,velRuedaDer, velRuedaIzq):
		self.pwm.set_pwm(0, 0, self.servo_min)
		self.pwm.set_pwm(1, 0, self.servo_max)
		time.sleep(segundos)
		self.parada()
	
	def atras(self, segundos,velRuedaDer, velRuedaIzq):
		self.pwm.set_pwm(0, 0, self.servo_max)
		self.pwm.set_pwm(1, 0, self.servo_min)
		time.sleep(segundos)
		self.parada()
		
	def giroDer(self, segundos,velRuedaDer, velRuedaIzq):
		self.pwm.set_pwm(0, 0, self.servo_max)
		self.pwm.set_pwm(1, 0, self.servo_max)
		time.sleep(segundos)
		self.parada()
		
	def giroIzq(self, segundos,velRuedaDer, velRuedaIzq):
		self.pwm.set_pwm(0, 0, self.servo_min)
		self.pwm.set_pwm(1, 0, self.servo_min)
		time.sleep(segundos)
		self.parada()
		


 
if __name__ == '__main__':
    
    robot = MovimientoRobot()
    robot.giroDer(1, 100, 100)

    


		
   


