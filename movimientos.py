import pygame

def movimientos(event,matriz):
    contador = 0
    posicion_cero = []
    limite = len(matriz)
    
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna][0]==0:
                posicion_cero = [fila,columna]

    if event.type == pygame.KEYDOWN:  
        if event.key == pygame.K_w or event.key == pygame.K_UP:#Tecla W y felcha arriba 
            if not posicion_cero[0]==0:
                matriz[posicion_cero[0]][posicion_cero[1]],matriz[posicion_cero[0]-1][posicion_cero[1]] = matriz[posicion_cero[0]-1][posicion_cero[1]],matriz[posicion_cero[0]][posicion_cero[1]]
                contador = contador+1
                  
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:#Tecla A y flecha izquierda
            if not posicion_cero[1]==0:
                matriz[posicion_cero[0]][posicion_cero[1]],matriz[posicion_cero[0]][posicion_cero[1]-1] = matriz[posicion_cero[0]][posicion_cero[1]-1],matriz[posicion_cero[0]][posicion_cero[1]]
                contador = contador+1
                
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:#Tecla D y flecha derecha
            if not posicion_cero[1]==limite-1:
                matriz[posicion_cero[0]][posicion_cero[1]],matriz[posicion_cero[0]][posicion_cero[1]+1] = matriz[posicion_cero[0]][posicion_cero[1]+1],matriz[posicion_cero[0]][posicion_cero[1]]
                contador = contador+1
                    
        if event.key == pygame.K_s or event.key == pygame.K_DOWN: #Tecla S y flecha abajo
            if not posicion_cero[0]==limite-1:
                matriz[posicion_cero[0]][posicion_cero[1]],matriz[posicion_cero[0]+1][posicion_cero[1]] = matriz[posicion_cero[0]+1][posicion_cero[1]],matriz[posicion_cero[0]][posicion_cero[1]]
                contador = contador+1
    return contador    
