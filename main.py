import pygame
import sys
from matriz import *
from movimientos import *
from database import *

ancho_ventana = 800
alto_ventana = 1000

#Inicio interface grafica 
ventana = pygame.display.set_mode((ancho_ventana,alto_ventana))
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
    global estado_juego

    #constantes
    PUNTO_X_CUADRO = 250
    PUNTO_Y_CUADRO = 363

    #...
    texto_nombre = ""
    texto_contraseña = ""

    ingrese_usuario = "Usuario"
    ingrese_contraseña = "Contraseña"

    #Estados
    estado_cuadro_nombre = False
    estado_cuadro_contraseña = False

    #Fuentes
    fuente = pygame.font.Font(None,40)

    #Surface
    vetanap = pygame.Surface((800,1000))
    vetanap.fill(ROJO)
    ventana.blit(vetanap,(0,0))

    #Cuadros de entrada de datos 
    cuadro_nombre = pygame.Rect(PUNTO_X_CUADRO,PUNTO_Y_CUADRO,300,75)
    cuadro_contraseña = pygame.Rect (PUNTO_X_CUADRO,PUNTO_Y_CUADRO+100,300,75)
    cuadro_boton_ingreso = pygame.Rect (PUNTO_X_CUADRO+50,PUNTO_Y_CUADRO+200,200,60)
    cuadro_boton_registro = pygame.Rect(PUNTO_X_CUADRO+50,PUNTO_Y_CUADRO+270,200,25)

    #Dibuja los cuadros 
    pygame.draw.rect(ventana,(255,255,255),cuadro_nombre)
    pygame.draw.rect(ventana,(255,255,255),cuadro_contraseña)
    pygame.draw.rect(ventana,(50,255,0),cuadro_boton_ingreso)
    pygame.draw.rect(ventana,(150,0,0),cuadro_boton_registro)

    pygame.display.flip()
    inicio=True
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inicio=False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if cuadro_nombre.collidepoint(event.pos):
                    ingrese_usuario = ""
                    estado_cuadro_nombre = True
                    #Agregar algo como cambio de color...
                else:
                    if texto_nombre == "":
                        ingrese_usuario = "Usuario"
                    estado_cuadro_nombre  = False   

                if cuadro_contraseña.collidepoint(event.pos):
                    ingrese_contraseña = ""
                    estado_cuadro_contraseña = True
                    #Agregar algo como cambio de color...
                else:
                    if texto_contraseña =="":
                        ingrese_contraseña = "Contraseña"
                    estado_cuadro_contraseña  = False 

                if cuadro_boton_ingreso.collidepoint(event.pos):
                    if comprobar_contraseña(texto_nombre,texto_contraseña):
                        estado_juego = "juego"
                        inicio = False
                        break
                    else:
                        print("Hay algo mal")

                if cuadro_boton_registro.collidepoint(event.pos):
                    print("cambio a registro")
                    estado_juego = "registro"
                    inicio = False 
                    break

            if (event.type == pygame.KEYDOWN) and (estado_cuadro_nombre):
                if event.key == pygame.K_RETURN:
                    None
                    #modificar este apartado para los usuarios y contraseñas 
                elif event.key == pygame.K_BACKSPACE:
                    texto_nombre = texto_nombre[:-1]
                    #modificar este apartado para los usuarios y contraseñas 
                else:
                    texto_nombre += event.unicode

            if (event.type == pygame.KEYDOWN) and (estado_cuadro_contraseña):
                if event.key == pygame.K_RETURN:
                    None
                    #modificar este apartado para los usuarios y contraseñas 
                elif event.key == pygame.K_BACKSPACE:
                    texto_contraseña = texto_contraseña[:-1]
                    #modificar este apartado para los usuarios y contraseñas 
                else: 
                    texto_contraseña += event.unicode
        
        ventana.blit(vetanap,(0,0))

        pygame.draw.rect(ventana,(255,255,255),cuadro_nombre)
        pygame.draw.rect(ventana,(255,255,255),cuadro_contraseña)
        pygame.draw.rect(ventana,(50,255,0),cuadro_boton_ingreso)
        pygame.draw.rect(ventana,(150,0,0),cuadro_boton_registro)

        texto_nombre_surface = fuente.render(texto_nombre,True,(0,0,0))
        ventana.blit(texto_nombre_surface,(PUNTO_X_CUADRO,PUNTO_Y_CUADRO))  

        texto_contraseña_surface = fuente.render(texto_contraseña,True,(0,0,0)) 
        ventana.blit(texto_contraseña_surface,(PUNTO_X_CUADRO,PUNTO_Y_CUADRO+100))

        ingrese_nombre_surface = fuente.render(ingrese_usuario,True,(0,0,0))
        ventana.blit(ingrese_nombre_surface,(PUNTO_X_CUADRO,PUNTO_Y_CUADRO))

        ingrese_contraseña_surface = fuente.render(ingrese_contraseña,True,(0,0,0)) 
        ventana.blit(ingrese_contraseña_surface,(PUNTO_X_CUADRO,PUNTO_Y_CUADRO+100))

        pygame.display.flip()     

def main_registro():
    global estado_juego
    
    fondo = pygame.Surface((ancho_ventana,alto_ventana))

    fondo.fill((85,33,15))

    ventana.blit(fondo,(0,0))

    cuadro_nombre_registro = pygame.Rect(250,375,300,50)
    cuadro_contraseña_resgistro = pygame.Rect(250,475,300,50)
    cuadro_contraseña_resgistro_confirmar =pygame.Rect(250,575,300,50)
    cuadro_boton_registro = pygame.Rect(255,675,290,25)

    fuente = pygame.font.Font(None,40)

    texto_nombre = ""
    texto_contraseña = ""
    texto_confirmar = ""
    ingrese_nombre = "Usuario"
    ingrese_contraseña = "Contraseña"
    confirme_contraseña = "Confirme contraseña"

    estado_nombre = False
    estado_contraseña = False
    estado_confirmar = False

    pygame.draw.rect(ventana,(255,255,255),cuadro_nombre_registro)
    pygame.draw.rect(ventana,(255,255,255),cuadro_contraseña_resgistro)
    pygame.draw.rect(ventana,(255,255,255),cuadro_contraseña_resgistro_confirmar)
    pygame.draw.rect(ventana,(255,255,255),cuadro_boton_registro)

    pygame.display.flip()

    algo = True
    while algo == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                algo = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cuadro_nombre_registro.collidepoint(event.pos):
                    ingrese_nombre = ""
                    estado_nombre = True
                else:
                    estado_nombre = False
                    if texto_nombre == "":
                        ingrese_nombre = "Usuario"

                if cuadro_contraseña_resgistro.collidepoint(event.pos):
                    ingrese_contraseña = ""
                    estado_contraseña = True
                else:
                    if texto_contraseña == "":
                        ingrese_contraseña = "Contraseña"
                    estado_contraseña = False   

                if cuadro_contraseña_resgistro_confirmar.collidepoint(event.pos):
                    confirme_contraseña = ""
                    estado_confirmar = True
                else:
                    if texto_confirmar == "":
                        confirme_contraseña ="Confirme contraseña"
                    estado_confirmar = False

                if cuadro_boton_registro.collidepoint(event.pos):
                    if (texto_nombre != "" and texto_contraseña !="" and texto_confirmar != "") and (texto_contraseña == texto_confirmar):
                        registrar_usuario(texto_nombre,texto_confirmar)
                        estado_juego = "inicio"
                        algo = False 
                        break
                    
                    #decidir si hacer que regrese al inicio e ingrege el usuario nuevamente desde este boton o hacer que solo guarde los datos
                    #en la base de datos y que desde otro boton regrese al inicio
            
            if (event.type == pygame.KEYDOWN) and (estado_nombre):
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_BACKSPACE:
                    texto_nombre = texto_nombre[:-1]
                else:
                    texto_nombre += event.unicode

            if (event.type == pygame.KEYDOWN) and (estado_contraseña):
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_BACKSPACE:
                    texto_contraseña = texto_contraseña[:-1]
                else:
                    texto_contraseña += event.unicode

            if (event.type == pygame.KEYDOWN) and (estado_confirmar):
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_BACKSPACE:
                    texto_confirmar = texto_confirmar[:-1]
                else:
                    texto_confirmar += event.unicode

        ventana.blit(fondo,(0,0))
        pygame.draw.rect(ventana,(255,255,255),cuadro_nombre_registro)
        pygame.draw.rect(ventana,(255,255,255),cuadro_contraseña_resgistro)
        pygame.draw.rect(ventana,(255,255,255),cuadro_contraseña_resgistro_confirmar)
        pygame.draw.rect(ventana,(255,255,0),cuadro_boton_registro)

        texto_nombre_registro_surface = fuente.render(texto_nombre,True,(0,0,0))
        ventana.blit(texto_nombre_registro_surface,(250,375))

        texto_nombre_contraseña_surface = fuente.render(texto_contraseña,True,(0,0,0))
        ventana.blit(texto_nombre_contraseña_surface,(250,475))

        texto_confirmar_registro_surface = fuente.render(texto_confirmar,True,(0,0,0))
        ventana.blit(texto_confirmar_registro_surface,(250,575))

        ingrese_nombre_surface = fuente.render(ingrese_nombre,True,(100,0,0))
        ventana.blit(ingrese_nombre_surface,(250,375))

        ingrese_contraseña_surface = fuente.render(ingrese_contraseña,True,(100,0,0))
        ventana.blit(ingrese_contraseña_surface,(250,475))

        confirme_contraseña_surface = fuente.render(confirme_contraseña,True,(100,0,0))
        ventana.blit(confirme_contraseña_surface,(250,575))

        pygame.display.flip() 
    pygame.QUIT 

estados =True
while estados:
    
    if estado_juego == "juego":
        main_juego()
    if estado_juego == "inicio":
        main_inicio()
    if estado_juego == "registro":
        main_registro()    
   