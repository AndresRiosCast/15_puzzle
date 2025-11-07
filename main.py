import pygame
import sys
from matriz import *
from movimientos import *        

#Inicio interface grafica 
ventana = pygame.display.set_mode((800,1000))
pygame.display.set_caption("Mi 15 PUZZLE")

#Colores
GRIS = (50, 50, 50)
ROJO = (245,0,0)
AZUL_TRASNSPARENTE = (0, 0, 255, 128)

#Estados
estado_juego = "inicio"

def main_juego():

    #Zonas de la interface de juego
    hoja_superior = pygame.Surface((1000,200))
    hoja_tablero = pygame.Surface((800,800))
    hoja_ganador = pygame.Surface((800,800), pygame.SRCALPHA) #hoja_ganador de color para efecto 

    #Coloreo
    hoja_superior.fill(GRIS)
    hoja_ganador.fill(AZUL_TRASNSPARENTE)

    #Asignacion de surfaces (zonas) a la ventana principal
    ventana.blit(hoja_superior,(0,0))
    ventana.blit(hoja_tablero,(0,200))

    #Fuentes de numeros_tablero
    fuente = pygame.font.Font(None,80)
    fuente2 = pygame.font.Font(None,40)

    #textos 
    texto_ganador = fuente.render("Tablero RESUELTO!!",True,(255,255,255))

    #Centrado de textos
    texto_ganador_centrado = texto_ganador.get_rect(center=(400,400))

    #variables utiles
    contador_uno = 0

    #Variables
    tamaño = 3 # Tamaño fijo para pruebas (cambiar a input si quieres) (mayor que 3 menor que 11)
    matriz,matriz_solucion = crear_matriz(tamaño,hoja_tablero)
    ancho, alto = matriz[0][0][1].get_size() #saca el ancho y alto de un surface del tablero ya que todos son del mismo tamaño

    juego_activo=True
    #Bucle de juego
    while juego_activo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                contador_uno += movimientos(event,matriz)
            if event.type == pygame.QUIT:
                juego_activo=False
                sys.exit()

        for fila in range(len(matriz)):
            for columna in range(len(matriz)):
                ventana.blit(matriz[fila][columna][1], (columna * ancho, fila * alto + 200))

        #Contador
        ventana.blit(hoja_superior,(0,0))
        Contador = fuente2.render("Movimientos: " + str(contador_uno), True, (255, 255, 255))  # blanco
        Contador_a = Contador.get_rect(center=(110,20 ))
        ventana.blit(Contador, Contador_a)

        if matriz == matriz_solucion: #Cuando Gana
            hoja_ganador.blit(texto_ganador,texto_ganador_centrado)
            ventana.blit(hoja_ganador,(0,200))
    
        pygame.display.flip()        
    pygame.quit()

def main_inicio():
    vetanap = pygame.Surface((800,1000))
    vetanap.fill(ROJO)
    ventana.blit(vetanap,(0,0))
    pygame.display.flip()
    inicio=True
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inicio=False
                sys.exit()
        pygame.display.flip()  
    pygame.quit()    
        
estados =True
while estados:
    
    if estado_juego == "juego":
        main_juego()
    if estado_juego == "inicio":
        main_inicio()
    