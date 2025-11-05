import pygame
import random

pygame.init()

def crear_matriz (tamaño,hoja_tablero): 

    ancho,alto = hoja_tablero.get_size() 
    tamaño_celda = int(ancho / tamaño)
    matriz = [] 
    contador = 0

    ancho_cortador = 0
    alto_cortador = 0

    for i in range(tamaño): #Crea la matriz tablero 
        filas = []  

        for u in range(tamaño):
            columna = []
            celda_tablero = pygame.Surface((tamaño_celda,tamaño_celda))
            
            if contador == (tamaño * tamaño)-1:
                columna.append(0)
                columna.append(celda_tablero)
            else:
                contador +=1
                columna.append(contador) 
                columna.append(celda_tablero)
            filas.append(columna)
            ancho+=ancho
        matriz.append(filas)

    matriz_solucion = [fila[:] for fila in matriz] #Crea una compia del tablero cuando esta resuelto

    agregar_imagen(matriz)

    for i in matriz: # Desorganiza el tablero
        random.shuffle(i)
    random.shuffle(matriz)
    
    alto +=alto
    return matriz,matriz_solucion 

def mostrar_matriz(matriz):
    for i in matriz:
        print(i)

def agregar_imagen(matriz):
    #Carga la imagen
    imagen = pygame.image.load("imagenes/gato.jpg")

    ancho, alto = matriz[0][0][1].get_size()

    GRIS = (50, 50, 50)

    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            matriz[fila][columna][1].fill(GRIS)
            tite0 = imagen.subsurface(pygame.Rect(columna*ancho,fila*ancho,ancho,ancho))
            if matriz[fila][columna][0]==0:
                matriz[fila][columna][1].fill(GRIS)
            else:
                matriz[fila][columna][1].blit(tite0,(0,0))

    return matriz