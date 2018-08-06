# -*- coding: cp1252 -*-

#         _\|/_
#         (O-O)
# -----oOO-(_)-OOo----------------------------------------------------


#######################################################################
# ******************************************************************* #
# *                                                                 * #
# *                   Autor:  Eulogio López Cayuela                 * #
# *                                                                 * #
# *                 Deteccion de una baliza luminosa                * #
# *                                                                 * #
# *                  Versión 1.1   Fecha: 01/08/2018                * #
# *                                                                 * #
# ******************************************************************* #
#######################################################################


'''
NOTAS:
    - pyton 2.7
    - SimpleCV


Deteccion/Seguimiento de una baliza led.

 
'''


print __doc__

from SimpleCV import Image, Camera, Color, DrawingLayer, Display
import time


class BusquedaBaliza:
	
	def __init__(self, webCam):
		
		self.webCam = webCam
		#reserva de fotograma con el que ir haciendo comparaciones
		self.captura_old = webCam.getImage()


		#Bandera para mostar la imagen real con el objetido resaltado /si TRUE)
		# o una imagen negra con un punto que representa la baliza (FALSE)

		self.FLAG_mostar_original = False


	def buscarBaliza(self):
		# capturar un fotograma 
		captura = self.webCam.getImage()
		if self.FLAG_mostar_original == True:
			original = captura

		
		captura = captura.colorDistance((255,255,255)).invert().stretch(230, 255)
		captura = captura.erode(1)

		#buscar diferencias entre el frame actual y el frame anterior
		baliza = self.captura_old - captura
		#realizar mejoras para la deteccion

		baliza = baliza.erode(1) #Mejora los falsos positivos pero perdemos distancia de deteccion (rango de un par de metros)
		baliza = baliza.dilate(8)

		#guardar el frame actual para la siguiente iteracion
		captura_old = captura
		
		#buscar objetos de interes y marcarlos
		blobs = baliza.findBlobs()
		if blobs:
			if blobs[-1].area()> 5:
				baliza.drawCircle((blobs[-1].x, blobs[-1].y), 20,Color.BLUE,5)
				if self.FLAG_mostar_original == True:
					original.drawCircle((blobs[-1].x, blobs[-1].y), 20,Color.BLUE,5)
					return original
				return baliza
		else:
			return None


