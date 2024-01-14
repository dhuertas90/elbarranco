import pygame
from pygame.locals import *
import random, time, sys
sys.path.append("./modules/")
import Mod_bot as bot, Mod_jue as jue, Mod_pj as per, Mod_ran as ran

GANADOR_PATH = "data/ganador.png"
GAMEOVER_PATH = "data/gameover.png"
GAMEOVER1_PATH = "data/gameover1.png"

FONDO_RELOJ_PATH = "data/reloj1.png"
VIDA_X, VIDA_Y = 53, 18
NIVEL_X, NIVEL_Y = 154, 15
PUNTOS_X, PUNTOS_Y = 280, 15
RELOJ_X, RELOJ_Y = 670, 8

FUENTE_PATH = "data/dejavu.ttf"
FONDO_NIVEL_A = "data/fondojuego.png"
FONDO_NIVEL_B = "data/fondojuego2.png"
FONDO_NIVEL_C = "data/fondojuego3.png"

valores = {}

def calcular_puntaje(valores_juego):
    bonus_inferior = 5 if valores['op'] == '-' else 2
    bonus_superior = 3 if valores['op'] == '-' else 1

    if valores_juego['cuentas'] <= 6:
        points = 2 * valores_juego['nivel'] + bonus_inferior
    else:
        points = 1 * valores_juego['nivel'] + bonus_superior

    return points

# def pos_botones():
#     # posición de los botones/opciones
#     lista = [250, 310, 370]
    
#     # Seleccionar una posición aleatoria inicial
#     p1 = random.randint(0, 2)
    
#     # Obtener las otras dos posiciones de manera única
#     posiciones_restantes = [i for i in range(3) if i != p1]
#     p2, p3 = random.sample(posiciones_restantes, 2)
    
#     # Asignar las posiciones de la lista según los índices obtenidos
#     p1, p2, p3 = lista[p1], lista[p2], lista[p3]
#     return p1, p2, p3

def pos_botones():
    # posicion de los botones/opciones 
    lista = [250, 310, 370]
    p1 = random.randint(0, 2)
    if p1 == 0:
        p2 = random.randint(1, 2)
        p3 = 2 if p2==1 else 1
    elif p1 == 2:
        p2 = random.randint(0, 1)
        p3 = 1 if p2==0 else 0
    else:
        p2 = random.randint(0, 1)
        if p2 == 0:
            p3 = 2
        else:
            p2, p3 = 2, 0
    p1, p2, p3 = lista[p1], lista[p2], lista[p3]
    return p1, p2, p3

def imprimir(texto, x, y, pantalla, tam=20):
    fuente = pygame.font.Font(FUENTE_PATH, tam)
    mensaje = fuente.render(texto, 1, (55, 55, 55))
    pantalla.blit(mensaje, (x, y))

def contador(num):
    return (num + 1) % 6


def seleccionar_fondo(nivel):
    if nivel <= 2:
        fondo = FONDO_NIVEL_A
    elif 2 < nivel < 5:
        fondo = FONDO_NIVEL_B
    else:
        fondo = FONDO_NIVEL_C
    return fondo

def correccion_respuesta(pantalla, personaje, juego, valores_juego):
    valores_juego['cuentas'] += 1
    if valores_juego['error'] == 0:
        # Respuesta correcta
        if valores_juego['op'] == '+':
            valores_juego['sumas'] += 1
        else:
            valores_juego['restas'] += 1
        valores_juego['correctas'] += 1
        personaje.Saltar(pantalla)
    else:
        # respuesta incorrecta
        juego.set_vidas(valores_juego['vidas'] - 1)
        valores_juego['vidas'] -= 1
        personaje.Caer(pantalla)

def contador_segundos(pantalla, fondo_tiempo, segundos,
                        un_segundo, mas60, seg, listo=False):
    # Contador de segundos - 60 milisegundos por segundo
    if time.localtime().tm_sec != segundos:
        un_segundo += 1
        if un_segundo == mas60:
            seg += 1
            tex = str(seg)
            pantalla.blit(fondo_tiempo, (670, 8))
            pygame.display.update()
            imprimir(tex, 685, 20, pantalla, tam=25)
            mas60 += 60
        if un_segundo == 900:
            # 15 segundos
            listo = True
    return pantalla, un_segundo, seg, mas60, listo

def analizar_nivel_actual(juego, v, gano=False):
    if v['correctas'] == 6 and v['nivel'] < 5:
        v['nivel'] += 1
        juego.set_nivel(v['nivel'])
        v['sumas'] = v['restas'] = v['correctas'] = v['cuentas'] = 0
    elif v['correctas'] == 6 and v['nivel'] == 5:
        gano = True

    return juego, gano

def mostrar_ganador(pantalla, juego):
    fondo_ganador = pygame.image.load(GANADOR_PATH)
    imprimir('¡G A N A S T E !', 290, 300, fondo_ganador, tam=25)
    imprimir(str(juego.get_puntaje()) + ' puntos', 290, 350, fondo_ganador, tam=25)
    pantalla.blit(fondo_ganador, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)

def mostrar_perdedor(pantalla):
    fondo_gameover = pygame.image.load(GAMEOVER_PATH)
    fondo_gameover1 = pygame.image.load(GAMEOVER1_PATH)
    
    for _ in range(0, 50):
        pantalla.blit(fondo_gameover, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)
        pantalla.blit(fondo_gameover1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)
    
    pygame.time.delay(200)

def finalizar_juego(pantalla, ran, juego, apodo, gano):
    ran.add_to_ranking(juego.get_puntaje(), apodo)
    if gano:
        mostrar_ganador(pantalla, juego)
    else:
        mostrar_perdedor(pantalla)

def cargar_fondo_nivel(nivel):
    fondo_nivel = seleccionar_fondo(nivel)
    return pygame.image.load(fondo_nivel)

def cargar_fondo_reloj():
    return pygame.image.load(FONDO_RELOJ_PATH)

def cargar_pantalla(pantalla, juego):
    fondo_nivel = cargar_fondo_nivel(juego.get_nivel())
    fondo_tiempo = cargar_fondo_reloj()
    pantalla.blit(fondo_nivel, (0, 0))
    pantalla.blit(fondo_tiempo, (RELOJ_X, RELOJ_Y))

    imprimir(str(juego.get_vidas()), VIDA_X, VIDA_Y, pantalla)
    imprimir(f"{juego.get_nivel()}    Nivel", NIVEL_X, NIVEL_Y, pantalla)
    imprimir(f"{juego.get_puntaje()} Puntos", PUNTOS_X, PUNTOS_Y, pantalla)

    return pantalla, fondo_nivel, fondo_tiempo


def creacion_botones(pantalla, pos1, pos2, pos3, res):
    # creacion de los botones
    b1, b2 = pygame.image.load("data/bot.png"), pygame.image.load("data/bot2.png")
    boton = bot.BotonNumero(b1, b2, 620, pos1, res, pantalla)
    b1, b2 = pygame.image.load("data/bot.png"), pygame.image.load("data/bot2.png")
    boton1 = bot.BotonNumero(b1, b2, 620, pos2, res + 5, pantalla)
    b1, b2 = pygame.image.load("data/bot.png"), pygame.image.load("data/bot2.png")
    boton2 = bot.BotonNumero(b1, b2, 620, pos3, res - 5, pantalla)
    sonido = bot.BotonSonido(685, 450, pantalla)
    return boton, boton1, boton2, sonido

def cargar_objetos_fondo(pantalla, juego, pos1, pos2, pos3, v):
    res, v['op'] = juego.cuenta(v['sumas'], v['restas'], v['cuentas'], pantalla)
    boton, boton1, boton2, sonido = creacion_botones(pantalla, pos1, pos2, pos3, res)
    return boton, boton1, boton2, sonido

def nuevo_juego(pantalla, sonidos, apodo, genero):
    pygame.display.set_caption('Jugando El Barranco...')
    cursor, juego, ranking = bot.Cursor(), jue.Juego(genero), ran.Ranking()
    gano = False
    valores['correctas'] = valores['cuentas'] = valores['sumas'] = valores['restas'] = 0
    valores['vidas'] = juego.get_vidas()
    valores['nivel'] = juego.get_nivel()

    while (valores['vidas'] > 0) and (gano is False):
        segundos = time.localtime().tm_sec
        mas60 = 60
        
        pantalla, fondo_nivel, fondo_tiempo= cargar_pantalla(pantalla, juego)     
        personaje = per.Personaje(juego.get_genero(), fondo_nivel)
        pos1, pos2, pos3 = pos_botones()

        # obtengo el resultado de la cuenta y el operador a utilizar
        boton, boton1, boton2, sonido = cargar_objetos_fondo(pantalla, juego, pos1, pos2, 
                                                                pos3, valores)
        # chequeo sonido activado y boton sonido
        if sonidos[2]==0 and sonido.sonido_activado():
            sonido.swich(sonidos, pantalla)
        # un_segundo es contador de segundos (60ms)
        # Inicializo error por tiempo
        un_segundo, seg, valores['error'], listo = 0, 0, 2, False 
        clock = pygame.time.Clock()

        while not listo:
            # Bucle esperando seleccion de respuesta del usuario
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    botones_mouse = pygame.mouse.get_pressed()
                    if botones_mouse[0] == 1:
                        if cursor.colliderect(boton.rect):
                            # Actualizar puntaje
                            puntos = calcular_puntaje(valores)
                            puntaje = juego.get_puntaje()
                            juego.set_puntaje(puntaje + puntos)
                            # Respuesta correcta
                            valores['error'], listo = 0, True
                        elif cursor.colliderect(boton1.rect) or cursor.colliderect(boton2.rect):
                            # Respuesta incorrecta
                            valores['error'], listo = 1, True
                        elif cursor.colliderect(sonido.rect):
                            sonido.swich(sonidos, pantalla)
                cursor.update()
                boton.update_numero(pantalla, cursor)
                boton1.update_numero(pantalla, cursor)
                boton2.update_numero(pantalla, cursor)
            pygame.display.flip()
            pantalla, un_segundo, seg, mas60, listo = contador_segundos(pantalla, fondo_tiempo, 
                                                                    segundos, un_segundo, mas60, seg, listo)
        personaje.Caminar(2, pantalla)
        correccion_respuesta(pantalla, personaje, juego, valores)
        juego, gano = analizar_nivel_actual(juego, valores, gano)
    finalizar_juego(pantalla, ranking, juego, apodo, gano)