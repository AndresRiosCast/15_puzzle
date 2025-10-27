import random
import pygame

pygame.init()

def crear_matriz (tamaño,zona_juego): #Resive un tamaño de matriz la crea y la organiza aleatoreamente

    ancho,alto = zona_juego.get_size() #optiene el ancho y alto del cuadro del Surface 
    tamaño_celda = int(ancho / tamaño) #reparte el tamaño de las celdas dividiendo el tamaño del tablero por la cantidad de celdas 
    matriz = [] 
    contador = 0

    for i in range(tamaño): #Ingresa en la matriz del tablero filas, columnas, valor y surface
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

    matriz_solucion = [fila[:] for fila in matriz] #Hace una copia de la matriz 

    for i in matriz: #Organiza de forma aleatorea la matriz 
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
        
        #Zonas de la interface
        panel_superior = pygame.Surface((1000,200))
        panel_lateral_derecho = pygame.Surface((200,850))
        panel_tablero = pygame.Surface((800,800))

        #Colores
        GRIS = (50, 50, 50)
        AZUL = (0, 100, 255)
        BLANCO = (255,255,255)
        ROJO = (255, 0, 0)  
        
        #Variables
        tamaño = 4  # Tamaño fijo para pruebas (cambiar a input si quieres)
        matriz,matriz_solucion = crear_matriz(tamaño,panel_tablero)

        #Inicio interface grafica 
        ventan = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("Mi 15 PUZZLE")
        juego_activo=True

        #Coloreo
        panel_superior.fill(GRIS)
        panel_lateral_derecho.fill(AZUL)
        panel_tablero.fill(BLANCO)

        #Asignacion de surfaces (zonas) a la ventana principal
        ventan.blit(panel_superior,(0,0))
        ventan.blit(panel_lateral_derecho,(800,205))
        ventan.blit(panel_tablero,(0,200))

        fuente = pygame.font.Font(None,80)

        ancho , alto = matriz[0][0][1].get_size() #saca el ancho y alto de un surface del tablero ya que todos son del mismo tamaño

        contador_uno = 0

        #Bucle de juego
        while juego_activo:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    contador_uno += movimientos(event,matriz)
                if event.type ==pygame.QUIT:
                    juego_activo=False

            for fila in range(len(matriz)):
                for columna in range(len(matriz)):
                    if matriz[fila][columna][0]==0:
                        matriz[fila][columna][1].fill(GRIS)
                    else:
                        matriz[fila][columna][1].fill(ROJO)

                    texto = fuente.render(str(matriz[fila][columna][0]), True, (255, 255, 255))  # blanco
                    rect_texto = texto.get_rect(center=(ancho // 2, alto // 2))
                    matriz[fila][columna][1].blit(texto, rect_texto)
                    pygame.draw.rect(matriz[fila][columna][1], (0,0,0), (0, 0, ancho, alto), 4)
                    ventan.blit(matriz[fila][columna][1], (columna * ancho, fila * alto + 200))

            #Contador
            ventan.blit(panel_superior,(0,0))
            Contador = fuente.render("Movimientos: " + str(contador_uno), True, (255, 255, 255))  # blanco
            Contador_a = Contador.get_rect(center=(250, alto // 2))
            ventan.blit(Contador, Contador_a)

            pygame.display.flip()
        pygame.quit()

main()
