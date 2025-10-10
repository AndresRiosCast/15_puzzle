import random
def crear_matriz (tamaño):
    matriz = []
    contador = 0
    for i in range(tamaño):
        filas = []  # Crear nueva lista para cada fila
        for u in range(tamaño):
            if contador == (tamaño * tamaño)-1:
                filas.append(0)
            else:
                contador +=1
                filas.append(contador)            
        matriz.append(filas)

    matriz_solucion = [fila[:] for fila in matriz]

    for i in matriz:
        random.shuffle(i)
    random.shuffle(matriz)
    
    return matriz,matriz_solucion

def mostrar_matriz(matriz):
    for i in matriz:
        print(i)

def movilidad(matriz,movimiento):
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

tamaño = int(input("Ingrese el tamaño que desea: "))
matriz,matriz_solucion = crear_matriz(tamaño)
mostrar_matriz(matriz)

while matriz != matriz_solucion:
    movimiento=str(input("Ingrese un movimiento (arriba,abajo,derecha,izquierda): "))
    mostrar_matriz(movilidad(matriz,movimiento))

