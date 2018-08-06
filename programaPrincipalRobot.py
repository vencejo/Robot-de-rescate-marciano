# -*- coding: cp1252 -*-

""" Programa de control de los robots simuladores de rescates marcianos

Autores:
Eulogio López Cayuela ( https://github.com/inopya )
Diego J. Mtez. Garcia

"""
from datetime import time as dtTime
from datetime import datetime
from datetime import timedelta
from SimpleCV import Display
from VideoBuffer_SimpleCV.Video_Signal_Delay import Video_Signal_Delay
from interfazControlRobot import interfazControlRobot
import time
from gestorEstados import GestorEstados

nombreRobot = "Curiosity"
puntuacion = 1000
minutosDeMision = 8

# Definir una instancia a la camara extraplanetaria
webCam =  Video_Signal_Delay(camara_id=1, retraso_video = 5, framerate=1.0, color=False, size=(640,480), ruido=True)

disp = Display()
interfazControl = interfazControlRobot( disp, minutosDeMision)
gestorEstados = GestorEstados(webCam, disp, interfazControl, puntuacion)
gestorEstados.iniciar()

tiempoInicioMision = datetime.now()
tiempoFinMision = tiempoInicioMision + timedelta(minutes=5)    



while disp.isNotDone():

	# leer un fotograma desde la camara video con retraso 
	# (para dificultar la visualizacion)
	imagen_diferido = webCam.video_remoto()
	interfazControl.imagen = imagen_diferido
	
	# Acepta ordenes solo si esta en el tiempo marcado para la mision
	tiempoActual = datetime.now()
	if tiempoActual < tiempoFinMision:
		listaOrdenes  = gestorEstados.procesarEstado()
		
	interfazControl.verInterfaz(nombreRobot, listaOrdenes, gestorEstados.verEstado(), gestorEstados.puntuacion)

	# video en directo para las funciones 
	# que hagan deteccion de objetos
	imagen_directo = webCam.getImage()
	
	imagen_diferido.save(disp)            


