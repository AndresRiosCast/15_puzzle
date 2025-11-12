import json

with open("data/datos.json","r") as base:
    datos = json.load(base)


def comprobar_contraseña(usuario,contraseña):
    for i in datos["usuarios"]:
        if i["usuario"]== usuario  and i["contrasena"] == contraseña:
            print("usuario correcto")
            return True

def registrar_usuario(usuario,contraseña):
    nuevo_usuario = {"usuario":usuario,"contrasena":contraseña}

    datos["usuarios"].append(nuevo_usuario)
    print(datos)    

    with open("data/datos.json","w") as base:
        json.dump(datos,base,indent=4)


