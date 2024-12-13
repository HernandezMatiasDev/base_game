import os
import time
import random

#tiempo de refresco para la consola
tiempo_refresco = 0.07

#ENSALADA DE FRUTAS
Banana=("\U0001F34C")
Sandia=("\U0001F349")
Frutilla=("\U0001F353")
Kiwi=("\U0001F95D")

#PASTA
Ajo=("\U0001F9C4")
Cebolla=("\U0001F9C5")
Tomate=("\U0001F345")
Pasta=("\U0001F35D")

#BURGA
Tomate=("\U0001F345")
Lechuga=("\U0001F96C")
Carne=("\U0001F969")
Pan=("\U0001F956")

#dificultades que tiene el juego
cant_niveles = ["nivel_1", "nivel_2", "nivel_3"]

niveles = {
    "nivel_1": [Banana, Sandia, Frutilla, Kiwi],
    "nivel_2": [Ajo, Cebolla, Tomate, Pasta],
    "nivel_3": [Tomate, Lechuga, Carne, Pan]
}

#un diccionario igual al de "niveles" para poder usarlo en mis funciones de debajo
frutas = {
    "nivel_1": ["Banana", "Sandia", "Frutilla", "Kiwi"],
    "nivel_2": ["Ajo", "Cebolla", "Tomate", "Pasta"],
    "nivel_3": ["Tomate", "Lechuga", "Carne", "Pan"]
}



filas_matriz_visual = 15
filas_matriz = 250
columnas_matriz = 100
punto =" "

tienda = """

             888888     88     888888     88b 88     8888b.         db    
               88       88     88__       88Yb88      8I  Yb       dPYb   
               88       88     88""       88 Y88      8I  dY      dP__Yb  
               88       88     888888     88  Y8     8888Y"      dP    Yb

TIENES: VAR00 Ingr
               
OPCIONES:                                
        MEJORAS:                 COSTO:     Niv Act:
       ╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╦ ═ ═ ═ ═ ═ ╦ ═ ═ ═ ═ ═ ╗
    1»  Caida de ingredientes:  VAR11 Ingr   NIV VAR31

    2»  Tamaño de contenedor:   VAR21 Ingr   NIV VAR41

    3»  Continuar recolectando
"""

victory =  """
                                             ██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗                                     
                                            ██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝                                     
                                            ██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗                                       
                                            ██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝                                       
                                            ╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗                                     
                                             ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝                                     
                                                                                                                                             
                ███████╗    ███████╗    ██╗         ██╗     ██████╗    ██╗    ██████╗      █████╗     ██████╗     ███████╗    ███████╗    ██╗
                ██╔════╝    ██╔════╝    ██║         ██║    ██╔════╝    ██║    ██╔══██╗    ██╔══██╗    ██╔══██╗    ██╔════╝    ██╔════╝    ██║
                █████╗      █████╗      ██║         ██║    ██║         ██║    ██║  ██║    ███████║    ██║  ██║    █████╗      ███████╗    ██║
                ██╔══╝      ██╔══╝      ██║         ██║    ██║         ██║    ██║  ██║    ██╔══██║    ██║  ██║    ██╔══╝      ╚════██║    ╚═╝
                ██║         ███████╗    ███████╗    ██║    ╚██████╗    ██║    ██████╔╝    ██║  ██║    ██████╔╝    ███████╗    ███████║    ██╗
                ╚═╝         ╚══════╝    ╚══════╝    ╚═╝     ╚═════╝    ╚═╝    ╚═════╝     ╚═╝  ╚═╝    ╚═════╝     ╚══════╝    ╚══════╝    ╚═╝"""


loose = """"
                        ███████ ██    ██ ███████ ██████  ████████ ███████     ██████   █████  ██████   █████      
                        ██      ██    ██ ██      ██   ██    ██    ██          ██   ██ ██   ██ ██   ██ ██   ██     
                        ███████ ██    ██ █████   ██████     ██    █████       ██████  ███████ ██████  ███████     
                             ██ ██    ██ ██      ██   ██    ██    ██          ██      ██   ██ ██   ██ ██   ██     
                        ███████  ██████  ███████ ██   ██    ██    ███████     ██      ██   ██ ██   ██ ██   ██     
                                                                                                                  
                                                                                                                  
                                ██       █████      ██████  ██████   ██████  ██   ██ ██ ███    ███  █████         
                                ██      ██   ██     ██   ██ ██   ██ ██    ██  ██ ██  ██ ████  ████ ██   ██        
                                ██      ███████     ██████  ██████  ██    ██   ███   ██ ██ ████ ██ ███████        
                                ██      ██   ██     ██      ██   ██ ██    ██  ██ ██  ██ ██  ██  ██ ██   ██        
                                ███████ ██   ██     ██      ██   ██  ██████  ██   ██ ██ ██      ██ ██   ██        
                                                                                                                  """


#submenu debajo del gameplay
gateto = """════════════════════════════════════════════════════════╦═════════════════════════════════════════════════════
 ____________________         _               _         ║
l                    l       /  \            / \        ║    INGREDIENTES RECOLECTADOS:
l   Escuchame, yo    l      /    \          /   \       ║   
l   quiero:          l     /      \        /     \      ║    TIENES: VAR00Ingr
l                    l    /        \______/       \     ║    
l  _FRUTA1_ : VAR10  l                             \    ║    
l                    l  $$$$$$$$$$$    $$$$$$$$$$   l   ║    -_FRUTA1_ : VAR11  
l  _FRUTA2_ : VAR20  l  $$        $    $       $$   l   ║    
l                    l  $$        $$$$$$       $$   l   ║    -_FRUTA2_ : VAR21 
l  _FRUTA3_ : VAR30  l  $$$$$$$$$$$___ $$$$$$$$$$   l   ║    
l                    l  \       ==(   )==           l   ║    -_FRUTA3_ : VAR31
l  _FRUTA4_ : VAR40   \  \         ---             /    ║    
l                       > \      ^i,^,,i^         /     ║    -_FRUTA4_ : VAR41
l____________________ /    \ ____________________/      ║"""


#reglas del juego para el usuario 
lore_reglas = """
Lore y Reglas:
=====================================================================================================
                                Bienvenido a Fruta Fest!
                        Eres el el cocinero peculiar de un peculiar restaurant.
        Tu objetivo es relizar el pedido de tus clientes gatos (si, los clientes son gatos).

        A lo largo del dia tendras 2 oportunidades para mejorar tu cocina: la cantidad de ingredientes
                                    y el tamaño de tu bowl de cocina.

        Existen 3 niveles, cada uno representa un dia difetente y cada uno tiene sus tematicas correspondientes.

                                        ¡Buena suerte!"
======================================================================================================
"""
#menu para el juego
show_menu=""" 
        Fruta Fest!
==================================
1. Comenzar juego
2. Salir
=================================="""


# Función principal del juego
print(lore_reglas)

def juego():
    querer_jugar = True
    while querer_jugar:
        print(show_menu)
        choice = pedir_datos(["1","2"], "ingrese una opcion del menu: ")
        os.system("cls")
        if choice == "1": 
            start_game()
        elif choice == "2":
            print("Gracias por jugar.")
            querer_jugar = False

def pedir_datos(dato,mensaje):
    bandera = True
    salida_de_datos = input(mensaje)
    while bandera:
        if salida_de_datos in dato:
            bandera = False
            return salida_de_datos
        else:
            salida_de_datos = input("Dato invalido, porfavor ingrese un dato valido: ")    

# Función para mover el canasto (o bowl) a lo largo del escritorio
def imprimir_en_coordenadas(texto, columnas):
    lineas = texto.split('\n')
    for linea in lineas:
        print(" " * columnas + linea)


#funcion para manterner a un texto ingresado de un largo predeterminado
def caracterizado(largo, caracter):
    caracter = str(caracter)
    while len(caracter) < largo:
        caracter = caracter + " "
    return caracter


#genera el submenu para el nivel (no la etapa)
def generar_cliente_submenu(nivel, puntajes):
    gateto_mod = gateto.replace("_FRUTA1_", caracterizado(8 ,frutas[nivel][0]))
    gateto_mod = gateto_mod.replace("VAR10", caracterizado(5 ,puntajes[nivel][0]))
    gateto_mod = gateto_mod.replace("_FRUTA2_", caracterizado(8 ,frutas[nivel][1]))
    gateto_mod = gateto_mod.replace("VAR20", caracterizado(5 ,puntajes[nivel][1]))
    gateto_mod = gateto_mod.replace("_FRUTA3_", caracterizado(8 ,frutas[nivel][2]))
    gateto_mod = gateto_mod.replace("VAR30", caracterizado(5 ,puntajes[nivel][2]))
    gateto_mod = gateto_mod.replace("_FRUTA4_", caracterizado(8 ,frutas[nivel][3]))
    gateto_mod = gateto_mod.replace("VAR40", caracterizado(5 ,puntajes[nivel][3]))
    return gateto_mod


#Funcion que actualiza los datos del submenu del gameplay (el que tiene el gato)
#       texto del menu, var total de frutas, fruta tipo1, fruta tipo 2, fruta tipo3, fruta tipo 4
def imprimir_cliente(sub_menu, var0, var1, var2, var3, var4):
    gateto_mod = sub_menu.replace("VAR00", caracterizado(5 ,var0))
    gateto_mod = gateto_mod.replace("VAR11", caracterizado(5 ,var1))
    gateto_mod = gateto_mod.replace("VAR21", caracterizado(5 ,var2))
    gateto_mod = gateto_mod.replace("VAR31", caracterizado(5 ,var3))
    gateto_mod = gateto_mod.replace("VAR41", caracterizado(5 ,var4))
    return gateto_mod


def generarMegaMatriz(stage, cant_frutas):
    #crear matriz
    matriz_obj = []
    frutas_del_nivel = []

    for i in range(filas_matriz):
        matriz_obj.append([punto])
        for z in range(columnas_matriz):
            matriz_obj[i].extend(punto)
    #insertar frutas en lugares random
    for i in range(cant_frutas):
        fruta_columna = random.choice(range(columnas_matriz))
        fruta_fila = random.choice(range(filas_matriz))
        fruta_valor = random.choice(niveles[stage])
        frutas_del_nivel.append((fruta_columna,fruta_fila, fruta_valor))

        matriz_obj[fruta_fila][fruta_columna] = fruta_valor
    frutas_del_nivel = sorted(frutas_del_nivel, key=lambda x: x[1])

    return matriz_obj, frutas_del_nivel


def start_game():
    #Los objetivos al que va a tener que alcanzar el usurio, fruta de tipo 1, fruta de tipo 2, etc..
    puntajes = {
        "nivel_1": [random.randint(10,25), random.randint(10,25), random.randint(10,25), random.randint(10,25)],
        "nivel_2": [random.randint(87,131), random.randint(87,131),random.randint(87,131), random.randint(87,131)],
        "nivel_3": [random.randint(1000,1500),random.randint(1000,1500), random.randint(1000,1500), random.randint(1000, 1500)]
    }
    
    cant_frutas_tot = 186
    bowl_long = 5
    contenedor_actual = f"""@@@{" " * bowl_long}@@@
  {"@" * (bowl_long + 2)}"""
    precios = [10, 10]
    mejoras = [1,1]
    frutas_recolec = [0, 0, 0, 0, 0]
    primer_pase = True
    victoria = True

    for lev in range(3):

        #condicional para pasar de nivel
            gasto = 0
            #fruta tipo 1, fruta tipo 2, fruta tipo 3, fruta tipo 4
            frutas_recolec[1] = 0
            frutas_recolec[2] = 0
            frutas_recolec[3] = 0
            frutas_recolec[4] = 0
            if victoria:
                for z in range(3):
                    compra = ""
                    matriz_objeto, frutas_del_nivel = generarMegaMatriz(cant_niveles[lev], cant_frutas_tot)
                    #genero al submenu con el cliente con los respectivos objetivos:
                    sub_menu = generar_cliente_submenu(cant_niveles[lev], puntajes)
                    mov = 0
                    rep = False
                    cantidad_de_frutas = len(frutas_del_nivel) - 1
                    for i in range(filas_matriz, 0, -1):
                        
                        # Extraer la submatriz
                        submatriz = [fila[:columnas_matriz] for fila in matriz_objeto[i : filas_matriz_visual + i ]]
                        #paso la matriz a texto para que se vea linda
                        matriz_str = "\n".join(["".join(map(str, fila)) for fila in submatriz])
                        print(matriz_str)

                        imprimir_en_coordenadas(contenedor_actual, mov)
                        if mov < 100 and rep == False:
                            mov = mov +2
                        else: rep = True
                        if mov > 0 and rep == True:
                            mov = mov -2
                        else: rep = False
                        
                        while i == (frutas_del_nivel[cantidad_de_frutas][1] - 15):
                            if frutas_del_nivel[cantidad_de_frutas][2] == niveles["nivel_" + str(lev+1)][0] and frutas_del_nivel[cantidad_de_frutas][0] >= mov and frutas_del_nivel[cantidad_de_frutas][0] <= mov + (bowl_long + 6):
                                frutas_recolec[1] += 1
                            elif frutas_del_nivel[cantidad_de_frutas][2] == niveles["nivel_" + str(lev+1)][1] and frutas_del_nivel[cantidad_de_frutas][0] >= mov and frutas_del_nivel[cantidad_de_frutas][0] <= mov + (bowl_long + 6):
                                frutas_recolec[2] += 1
                            elif frutas_del_nivel[cantidad_de_frutas][2] == niveles["nivel_" + str(lev+1)][2] and frutas_del_nivel[cantidad_de_frutas][0] >= mov and frutas_del_nivel[cantidad_de_frutas][0] <= mov + (bowl_long + 6):
                                frutas_recolec[3] += 1
                            elif frutas_del_nivel[cantidad_de_frutas][2] == niveles["nivel_" + str(lev+1)][3] and frutas_del_nivel[cantidad_de_frutas][0] >= mov and frutas_del_nivel[cantidad_de_frutas][0] <= mov + (bowl_long + 6):
                                frutas_recolec[4] += 1
                            cantidad_de_frutas = cantidad_de_frutas - 1

                        #aumentar el contador de frutas totales:
                        frutas_recolec[0] = frutas_recolec[1] + frutas_recolec[2] + frutas_recolec[3] + frutas_recolec[4] - gasto
                        
                        print(imprimir_cliente(sub_menu, frutas_recolec[0], frutas_recolec[1], frutas_recolec[2], frutas_recolec[3], frutas_recolec[4]))

                        time.sleep(tiempo_refresco)
                        os.system("cls")

                    #final de la simulacion y fase de compra:
                    if not(frutas_recolec[1] >= puntajes["nivel_"+ str(lev+1)][0] and frutas_recolec[2] >= puntajes["nivel_"+ str(lev+1)][1] and frutas_recolec[3] >= puntajes["nivel_"+ str(lev+1)][2] and frutas_recolec[4] >= puntajes["nivel_"+ str(lev+1)][3]) and z == 2:
                        victoria = False
                    while (compra != "3") and victoria and (lev != 2 and z != 2):
                        print(imprimir_cliente(tienda, frutas_recolec[0], precios[0], precios[1], mejoras[0], mejoras[1]))
                        compra = pedir_datos(["1", "2", "3"],"Ingrese una opcion: ")

                        if compra == "1": #caida de frutas
                            if frutas_recolec[0] >= precios[0]:
                                gasto = gasto + precios[0]
                                frutas_recolec[0] = frutas_recolec[0] - precios[0]
                                cant_frutas_tot = int(cant_frutas_tot * 1.5)
                                precios[0] = int(precios[0] * 3) - 5
                                mejoras[0] = mejoras[0] +1
                                print("COMPRA REALIZADA")

                            elif frutas_recolec[0] < precios[0]:
                                print("No tienes suficiente dinero, sigue recolectando ingredientes")

                        if compra == "2": #tamaño de contedor
                            if frutas_recolec[0] >= precios[1]:
                                gasto = gasto + precios[1]
                                bowl_long = bowl_long + 2
                                contenedor_actual = f"""@@@{" " * bowl_long}@@@
  {"@" * (bowl_long + 2)}"""
                                frutas_recolec[0] = frutas_recolec[0] - precios[1]
                                precios[1] = precios[1] * 2 -5
                                mejoras[1] = mejoras[1] +1
                                print("COMPRA REALIZADA")
                            elif frutas_recolec[0] < precios[1]:
                                print("No tienes suficiente dinero, sigue recolectando ingredientes")
                        
                        time.sleep(1)
                        os.system("cls")

    if victoria == True:
        print (victory)
        time.sleep(5)
    else:
        print(loose)
        time.sleep(5)

juego()