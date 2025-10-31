import random
import pygame

pygame.init()

def crear_matriz (tamaño,hoja_tablero): 

    ancho,alto = hoja_tablero.get_size() 
    tamaño_celda = int(ancho / tamaño)
    matriz = [] 
    contador = 0

    for i in range(tamaño): #crea la matriz tablero 
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
        matriz.append(filas)

    matriz_solucion = [fila[:] for fila in matriz] #Crea una compia del tablero cuando esta resuelto

    for i in matriz: #Desorganiza el tablero
        random.shuffle(i)
    random.shuffle(matriz)
    
    return matriz,matriz_solucion 

def mostrar_matriz(matriz):
    for i in matriz:
        print(i)

def movimiento(matriz,movimiento):
    for i in range(len(matriz)):
        for u in range(len(matriz[i])):
            if matriz[i][u] == 0:
                match movimiento:
                    case "arriba":
                        if i-1>-1:
                            matriz[i][u],matriz[i-1][u]=matriz[i-1][u], matriz[i][u]
                    case "abajo":
                        if i+1<(len(matriz)):
                            matriz[i][u],matriz[i+1][u]=matriz[i+1][u], matriz[i][u]
                    case "derecha":
                        if u+1<(len(matriz)):
                            matriz[i][u],matriz[i][u+1]=matriz[i][u+1], matriz[i][u]
                    case "izquierda":
                        if u-1>-1:
                            matriz[i][u],matriz[i][u-1]=matriz[i][u-1], matriz[i][u]                           
                return matriz
            
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
              
def main():
        #Inicio interface grafica 
        ventana = pygame.display.set_mode((800,1000))
        pygame.display.set_caption("Mi 15 PUZZLE")
        juego_activo=True

        #Colores
        GRIS = (50, 50, 50)
        AZUL = (0, 100, 255)
        BLANCO = (255,255,255)
        ROJO = (255, 0, 0)  
        
        #Zonas de la interface
        hoja_superior = pygame.Surface((1000,200))
        # hoja_derecha = pygame.Surface((200,850))
        hoja_tablero = pygame.Surface((800,800))
        hoja_ganador = pygame.Surface((800,800), pygame.SRCALPHA) #hoja_ganador de color para efecto 
        
        #Coloreo
        hoja_superior.fill(GRIS)
        # hoja_derecha.fill(AZUL)
        hoja_tablero.fill(BLANCO)
        hoja_ganador.fill((0, 0, 255, 128)) #Azul transparente

        #Asignacion de surfaces (zonas) a la ventana principal
        ventana.blit(hoja_superior,(0,0))
        # ventana.blit(hoja_derecha,(800,205))
        ventana.blit(hoja_tablero,(0,200))
        
        #Fuentes de numeros_tablero
        fuente = pygame.font.Font(None,80)
        fuente2= pygame.font.Font(None,40)

        #textos 
        texto_ganador = fuente.render("Tablero RESUELTO!!",True,(255,255,255))

        #Centrado de textos
        texto_ganador_centrado = texto_ganador.get_rect(center=(400,400))

        #variables utiles
        contador_uno = 0

        #Variables
        tamaño = 2 # Tamaño fijo para pruebas (cambiar a input si quieres) (mayor que 3 menor que 11)
        matriz,matriz_solucion = crear_matriz(tamaño,hoja_tablero)
        ancho, alto = matriz[0][0][1].get_size() #saca el ancho y alto de un surface del tablero ya que todos son del mismo tamaño

        #Bucle de juego
        while juego_activo:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    contador_uno += movimientos(event,matriz)
                if event.type == pygame.QUIT:
                    juego_activo=False

            for fila in range(len(matriz)):
                for columna in range(len(matriz)):
                    if matriz[fila][columna][0]==0:
                        matriz[fila][columna][1].fill(GRIS)
                    else:
                        matriz[fila][columna][1].fill(ROJO)

                    numeros_tablero = fuente.render(str(matriz[fila][columna][0]), True, (255, 255, 255))  # blanco
                    rect_numeros_tablero = numeros_tablero.get_rect(center=(ancho // 2, alto // 2))
                    matriz[fila][columna][1].blit(numeros_tablero, rect_numeros_tablero)
                    pygame.draw.rect(matriz[fila][columna][1], (0,0,0), (0, 0, ancho, alto), 4)
                    ventana.blit(matriz[fila][columna][1], (columna * ancho, fila * alto + 200))

            #Contador
            ventana.blit(hoja_superior,(0,0))
            Contador = fuente2.render("Movimientos: " + str(contador_uno), True, (255, 255, 255))  # blanco
            Contador_a = Contador.get_rect(center=(110,20 ))
            ventana.blit(Contador, Contador_a)

            if matriz == matriz_solucion:
                print("Lo lograste!")
                hoja_ganador.blit(texto_ganador,texto_ganador_centrado)
                ventana.blit(hoja_ganador,(0,200))
                
            pygame.display.flip()
        pygame.quit()
main()
