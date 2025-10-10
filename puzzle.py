def crearmatrix (tamaño):
    print (tamaño)
    matrix = []
    contador = 0
    for i in range(tamaño):
        filas = []  # Crear nueva lista para cada fila
        for u in range(tamaño):
            if contador == (tamaño * tamaño)-1:
                filas.append(0)
            else:
                contador +=1
                filas.append(contador)            
        matrix.append(filas)
    return matrix

def mostrar_matriz(matriz):
    for i in matriz:
        print(i)

tamaño = int(input("Ingrese el tamaño que desea: "))
mostrar_matriz(crearmatrix(tamaño))

