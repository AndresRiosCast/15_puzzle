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

    for i in matriz: # Desorganiza el tablero
        random.shuffle(i)
    random.shuffle(matriz)
    
    alto +=alto
    return matriz,matriz_solucion 

def mostrar_matriz(matriz):
    for i in matriz:
        print(i)