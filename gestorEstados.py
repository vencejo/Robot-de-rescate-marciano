import time
from datetime import time as dtTime
from datetime import datetime
from datetime import timedelta
from movimientoRobot_Thymio import MovimientoRobot
from busqueda_baliza import BusquedaBaliza

class Visualizacion:
	
	def __init__(self, webCam,listaOrdenesPendientes, interfaz, robot):
		self.webCam  = webCam
		self.interfaz = interfaz
		self.robot = robot
		self.listaOrdenesPendientes = listaOrdenesPendientes
		self.nombreEstado = "visualizacion"
		self.tiempoInicioVisualizacion = datetime.now()
		self.siguienteVisualizacion = self.tiempoInicioVisualizacion + timedelta(seconds=1) 
		self.numOrdenes = len(listaOrdenesPendientes)  
		self.contOrdenesVisualizadas = 0
	
	def procesarEstado(self, gestor):

		self.interfaz.mostrarOrdenes(self.listaOrdenesPendientes)
		self.interfaz.mostrarRecuadroOrdenVisualizada(self.contOrdenesVisualizadas )
		
		tiempoActual = datetime.now()
		if tiempoActual > self.siguienteVisualizacion:
			self.siguienteVisualizacion = tiempoActual + timedelta(seconds=1)  
			self.contOrdenesVisualizadas += 1
			
		if self.numOrdenes <= self.contOrdenesVisualizadas :		
			gestor.estado = Planificacion(self.webCam , self.interfaz, self.robot)
			
		time.sleep(2)
		return None
		

class Recepcion:
	
	def __init__(self, webCam, listaOrdenesPendientes, interfaz, robot):
		self.webCam  = webCam
		self.interfaz = interfaz
		self.robot = robot
		self.listaOrdenesPendientes = listaOrdenesPendientes
		self.nombreEstado = "recepcion"
		self.tiempoInicioRecepcion = datetime.now()
		self.tiempoFinRecepcion = self.tiempoInicioRecepcion + timedelta(seconds=5) 
	
	def procesarEstado(self, gestor):		
		tiempoActual = datetime.now()
		if tiempoActual < self.tiempoFinRecepcion:
			time.sleep(1)
			print("Recepcionando...")
			return None
		else:
			gestor.estado = Visualizacion(self.webCam, self.listaOrdenesPendientes, self.interfaz, self.robot )
			return self.listaOrdenesPendientes

class Ejecucion:
	
	def __init__(self,webCam , listaOrdenesPendientes, interfaz, robot):
		self.webCam = webCam
		self.interfaz = interfaz
		self.robot = robot
		self.listaOrdenesPendientes = listaOrdenesPendientes
		self.nombreEstado = "ejecucion"
	
	def procesarEstado(self, gestor):
		print("Ejecutando Ordenes")
		
		for orden in self.listaOrdenesPendientes:
			
			observando = False
			
			if orden == "avance":
				print("avance")
				self.robot.avance(1,300,300)
			elif orden == "atras":
				print("atras")
				self.robot.atras(1,300,300)
			elif orden == "derecha":
				print("derecha")
				self.robot.giroDer(1, 100, 100)
			elif orden == "izquierda":
				print("izquierda")
				self.robot.giroIzq(1, 100, 100)
			elif orden == "observar":
				print("observar")
				observando = True
				imagenBaliza = BusquedaBaliza(self.webCam).buscarBaliza()
				if imagenBaliza != None:
					for i in range(8):
						self.webCam.video_buffer.append(imagenBaliza)
			
			# Descanso un segundo tras realizar la orden para poder tomar una buena foto
			time.sleep(2)
			if not observando:
				#Imagen Tras realizar la accion guardada en el buffer 
				# de imagenes pendientes para mostrar
				for i in range(6):
					imagen_directo_trasAccion = self.webCam.gris(self.webCam.getImage())
					self.webCam.video_buffer.append(imagen_directo_trasAccion)
				
		gestor.estado = Recepcion(self.webCam ,self.listaOrdenesPendientes, self.interfaz, self.robot)
		return self.listaOrdenesPendientes

class Envio:
	
	def __init__(self,webCam, listaOrdenesPendientes, interfaz, robot):
		self.webCam  = webCam
		self.interfaz = interfaz
		self.robot = robot
		self.listaOrdenesPendientes = listaOrdenesPendientes
		self.nombreEstado = "envio"
		self.tiempoInicioEnvio = datetime.now()
		self.tiempoFinEnvio = self.tiempoInicioEnvio + timedelta(seconds=5)   
		
	def procesarEstado(self, gestor):
		tiempoActual = datetime.now()
		if tiempoActual < self.tiempoFinEnvio:
			print("Enviando...")
			return None
		else:
			gestor.puntuacion = gestor.puntuacion - len(self.listaOrdenesPendientes)
			gestor.estado = Ejecucion(self.webCam ,self.listaOrdenesPendientes, self.interfaz,self.robot)
			return self.listaOrdenesPendientes

class Planificacion:
	
	def __init__(self, webCam, interfaz, robot):
		
		self.webCam = webCam
		self.interfaz = interfaz
		self.robot = robot
		self.numOrdenSiguiente = 1
		self.numOrdenesMax = 10
		self.listaOrdenesPendientes = []
		self.pausaEntreOrdenes = 2
		self.nombreEstado = "planificacion"

	
	def procesarEstado(self, gestor):
		if gestor.display.pressed != None :
			listaTeclas = list(gestor.display.pressed)
			try:
				codTeclaPresionada = listaTeclas.index(1)
				
				if codTeclaPresionada == 273 and self.numOrdenSiguiente <= self.numOrdenesMax:
					self.listaOrdenesPendientes.append("avance")
					self.numOrdenSiguiente += 1
				elif codTeclaPresionada == 274 and self.numOrdenSiguiente <= self.numOrdenesMax:
					self.listaOrdenesPendientes.append("atras")
					self.numOrdenSiguiente += 1
				elif codTeclaPresionada == 275 and self.numOrdenSiguiente <= self.numOrdenesMax:
					self.listaOrdenesPendientes.append("derecha")
					self.numOrdenSiguiente += 1
				elif codTeclaPresionada == 276 and self.numOrdenSiguiente <= self.numOrdenesMax:
					self.listaOrdenesPendientes.append("izquierda")
					self.numOrdenSiguiente += 1
				elif codTeclaPresionada == 111 and self.numOrdenSiguiente <= self.numOrdenesMax:
					self.listaOrdenesPendientes.append("observar")
					self.numOrdenSiguiente += 1
				elif codTeclaPresionada == 8 :
					self.listaOrdenesPendientes.pop()
					self.numOrdenSiguiente -= 1
				elif codTeclaPresionada == 13 :
					gestor.estado = Envio(self.webCam ,self.listaOrdenesPendientes, self.interfaz, self.robot)
				
			except:
				pass
				
		return self.listaOrdenesPendientes
	
	

class GestorEstados:
	
	def __init__(self, webCam, display, interfazControl, puntuacion):
		self.webCam = webCam
		self.display = display
		self.interfaz = interfazControl
		self.robot = MovimientoRobot()
		self.estado = Planificacion(self.webCam , self.interfaz,self.robot)
		self.puntuacion = puntuacion
		
		
	def iniciar(self):
		self.procesarEstado()	
		
	def verEstado(self):
		return self.estado.nombreEstado 
		
	def procesarEstado(self):
		resultado = self.estado.procesarEstado(self)
		return resultado
		
		
