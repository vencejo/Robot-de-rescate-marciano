from SimpleCV import Display, Image, Camera, Color, DrawingLayer
import time
from datetime import time as dtTime
from datetime import datetime
from datetime import timedelta


class interfazControlRobot():
	
	
	def __init__(self, display, minutosDeMision):
		
		self.imagen = None
		self.nivelBateria = "alto"
		self.display = display
		self.mostrarInterfaz = True
		self.coordsXOrdenes = [30, 80, 130,180,230,280,330,380,430,480]
		self.coordsYOrdenes = 50
		self.minutosDeMision = minutosDeMision
		self.tiempoInicioMision = datetime.now()
		self.tiempoMisionUnTercio = self.tiempoInicioMision + timedelta(minutes=minutosDeMision//3)    
		self.tiempoMisionMitad = self.tiempoInicioMision + timedelta(minutes= minutosDeMision//2)   
		self.tiempoMision = self.tiempoInicioMision + timedelta(minutes=minutosDeMision)   
		
		
	def mirarCodTeclaPulsada(self):
		if self.display.pressed != None:
			listaTeclas = list(self.display.pressed)
			try:
				codTeclaPresionada = listaTeclas.index(1)
				print(codTeclaPresionada)
			except:
				pass
				
	def mostrarInterfaz_siNo(self):
		if self.display.pressed != None :
			listaTeclas = list(self.display.pressed)
			try:
				codTeclaPresionada = listaTeclas.index(1)
				
				if codTeclaPresionada == 105: # tecla i
					self.mostrarInterfaz = not self.mostrarInterfaz

			except:
				return None
		
				
	def mostrarOrdenes(self, listaOrdenes):
		
		coordx = self.coordsXOrdenes[-1]
		coordy = self.coordsYOrdenes
		
		if listaOrdenes != None:
			for orden in listaOrdenes:
				if orden == "avance":
					self.mostrarOrdenAvance(coordx,coordy)
					coordx -= 50
				elif orden == "atras":
					self.mostrarOrdenAtras(coordx,coordy)
					coordx -= 50
				elif orden == "derecha":
					self.mostrarOrdenDerecha(coordx,coordy)
					coordx -= 50
				elif orden == "izquierda":
					self.mostrarOrdenIzquierda(coordx,coordy)
					coordx -= 50
				elif orden == "observar":
					self.mostrarOrdenObservar(coordx,coordy)
					coordx -= 50

		
			
		
	def mostrarNivelBateria(self, nivelBateria):
		# Los Niveles seran Alto, medio o bajo
			
		textoCoordx = 580
		textoCoordy = 420
		self.imagen.dl().setFontSize(20)
		
		if nivelBateria == "alto":
			# Pintando barra de bateria del robot
			self.imagen.dl().line((620,100), (620,400), Color.GREEN, width=10 )
			self.imagen.dl().text("Nivel", (textoCoordx,textoCoordy), color = Color.GREEN)
			self.imagen.dl().text("Bateria", (textoCoordx,textoCoordy + 10), color = Color.GREEN)
			self.imagen.dl().text("Robot", (textoCoordx,textoCoordy + 20), color = Color.GREEN)
			
		if nivelBateria == "medio":
			# Pintando barra de bateria del robot
			self.imagen.dl().line((620,200), (620,400), Color.ORANGE, width=10 )
			self.imagen.dl().text("Nivel", (textoCoordx,textoCoordy), color = Color.ORANGE)
			self.imagen.dl().text("Bateria", (textoCoordx,textoCoordy + 10), color = Color.ORANGE)
			self.imagen.dl().text("Robot", (textoCoordx,textoCoordy+20), color = Color.ORANGE)
			
		if nivelBateria == "bajo":
			# Pintando barra de bateria del robot
			self.imagen.dl().line((620,300), (620,400), Color.RED, width=10 )
			self.imagen.dl().text("Nivel", (textoCoordx,textoCoordy), color = Color.RED)
			self.imagen.dl().text("Bateria", (textoCoordx,textoCoordy + 10), color = Color.RED)
			self.imagen.dl().text("Robot", (textoCoordx,textoCoordy+20), color = Color.RED)
			
		if nivelBateria == "agotado":
			self.imagen.dl().text("Bateria", (textoCoordx,textoCoordy), color = Color.RED)
			self.imagen.dl().text("Robot", (textoCoordx,textoCoordy + 10), color = Color.RED)
			self.imagen.dl().text("Agotada", (textoCoordx,textoCoordy+20), color = Color.RED)
	
	
	def mostrarEstado(self,estado):
		
		self.imagen.dl().setFontSize(20)
		self.imagen.dl().text("Fases de Ejecucion", (20,110), color = Color.YELLOW)
		self.imagen.dl().text("planificacion", (20,140), color = Color.GREEN)
		self.imagen.dl().text("envio", (135,140), color = Color.YELLOW)
		self.imagen.dl().text("ejecucion", (200,140), color = Color.GREEN)
		self.imagen.dl().text("recepcion", (300,140), color = Color.YELLOW)
		self.imagen.dl().text("visualizacion", (400,140), color = Color.GREEN)
		
		self.imagen.dl().line((20,130), (530,130), Color.GREEN, width=2 )
		if estado == "planificacion":
			self.imagen.dl().line((20,130), (100,130), Color.GREEN, width=10 )
		elif estado == "envio":	
			self.imagen.dl().line((100,130), (200,130), Color.YELLOW, width=10 )
		elif estado == "ejecucion":
			self.imagen.dl().line((200,130), (300,130), Color.GREEN, width=10 )
		elif estado == "recepcion":	
			self.imagen.dl().line((300,130), (400,130), Color.YELLOW, width=10 )
		elif estado == "visualizacion":	
			self.imagen.dl().line((400,130), (530,130), Color.GREEN, width=10 )
				
			
	def mostrarRecuadroOrdenes(self):
		self.imagen.dl().setFontSize(20)
		self.imagen.dl().text("Ordenes", (20,20), color = Color.YELLOW)
		self.imagen.dl().rectangle((20,40), (510,60), Color.GREEN, width=5 )
		
	def mostrarOrdenAvance(self, esquinaArribaX, esquinaArribaY):
		self.imagen.dl().rectangle((esquinaArribaX,esquinaArribaY), (40,40), Color.GREEN, width=2)
		self.imagen.dl().line((esquinaArribaX,esquinaArribaY+40), (esquinaArribaX+20,esquinaArribaY), Color.YELLOW, width=2 )
		self.imagen.dl().line((esquinaArribaX+40,esquinaArribaY+40), (esquinaArribaX+20,esquinaArribaY), Color.YELLOW, width=2 )
		
	def mostrarOrdenAtras(self, esquinaArribaX, esquinaArribaY):
		self.imagen.dl().rectangle((esquinaArribaX,esquinaArribaY), (40,40), Color.GREEN, width=2)
		self.imagen.dl().line((esquinaArribaX,esquinaArribaY), (esquinaArribaX+20,esquinaArribaY+40), Color.YELLOW, width=2 )
		self.imagen.dl().line((esquinaArribaX+40,esquinaArribaY), (esquinaArribaX+20,esquinaArribaY+40), Color.YELLOW, width=2 )
		
	def mostrarOrdenDerecha(self, esquinaArribaX, esquinaArribaY):
		self.imagen.dl().rectangle((esquinaArribaX,esquinaArribaY), (40,40), Color.GREEN, width=2)
		self.imagen.dl().line((esquinaArribaX,esquinaArribaY), (esquinaArribaX+40,esquinaArribaY+20), Color.YELLOW, width=2 )
		self.imagen.dl().line((esquinaArribaX,esquinaArribaY+40), (esquinaArribaX+40,esquinaArribaY+20), Color.YELLOW, width=2 )
		
	def mostrarOrdenIzquierda(self, esquinaArribaX, esquinaArribaY):
		self.imagen.dl().rectangle((esquinaArribaX,esquinaArribaY), (40,40), Color.GREEN, width=2)
		self.imagen.dl().line((esquinaArribaX,esquinaArribaY+20), (esquinaArribaX+40,esquinaArribaY), Color.YELLOW, width=2 )
		self.imagen.dl().line((esquinaArribaX,esquinaArribaY+20), (esquinaArribaX+40,esquinaArribaY+40), Color.YELLOW, width=2 )
			
	def mostrarOrdenObservar(self, esquinaArribaX, esquinaArribaY):
		self.imagen.dl().rectangle((esquinaArribaX,esquinaArribaY), (40,40), Color.GREEN, width=2)
		self.imagen.dl().line((esquinaArribaX,esquinaArribaY+20), (esquinaArribaX+20,esquinaArribaY), Color.YELLOW, width=2 )
		self.imagen.dl().line((esquinaArribaX+20,esquinaArribaY), (esquinaArribaX+40,esquinaArribaY+20), Color.YELLOW, width=2 )
		self.imagen.dl().line((esquinaArribaX,esquinaArribaY+20), (esquinaArribaX+20,esquinaArribaY+40), Color.YELLOW, width=2 )
		self.imagen.dl().line((esquinaArribaX+20,esquinaArribaY+40), (esquinaArribaX+40,esquinaArribaY+20), Color.YELLOW, width=2  )
		self.imagen.dl().circle((esquinaArribaX + 20, esquinaArribaY+20), 10, Color.YELLOW, width = 2)
		
	def mostrarRecuadroOrdenVisualizada(self, numOrden):
		coordx = self.coordsXOrdenes[-1-numOrden]
		coordy = self.coordsYOrdenes
		self.imagen.dl().rectangle((coordx,coordy), (40,40), Color.RED, width=5 )
		
		
	
	def verNivelBateria(self):
		tiempoActual = datetime.now()
		if tiempoActual > self.tiempoMision:
			self.mostrarNivelBateria("agotado")
		elif tiempoActual > self.tiempoMisionMitad:
			self.mostrarNivelBateria("bajo")
		elif tiempoActual > self.tiempoMisionUnTercio:
			self.mostrarNivelBateria("medio")
		else:
			self.mostrarNivelBateria("alto")
			
	def verPuntuacion(self, puntos):
		textoCoordx = 540
		textoCoordy = 20
		self.imagen.dl().setFontSize(24)
		self.imagen.dl().text("Puntuacion", (textoCoordx,textoCoordy), color = Color.GREEN)
		self.imagen.dl().setFontSize(36)
		self.imagen.dl().text(str(puntos), (textoCoordx,textoCoordy + 30), color = Color.YELLOW)
		
	
	def mostrarNombreRobot(self, nombre):
		self.imagen.dl().setFontSize(20)
		self.imagen.dl().text("Nombre Robot:", (180,20), color = Color.GREEN)
		self.imagen.dl().setFontSize(30)
		self.imagen.dl().text(nombre, (290,15), color = Color.YELLOW)
			
			
	def verInterfaz(self, nombre, listaOrdenes, estado, puntuacion):
		self.mostrarInterfaz_siNo()
		if not self.mostrarInterfaz:
			return None
		self.mostrarNombreRobot(nombre)
		self.mostrarRecuadroOrdenes()
		self.mostrarOrdenes(listaOrdenes)
		self.mostrarEstado(estado)	
		self.verNivelBateria()	
		self.verPuntuacion(puntuacion)
		
	
