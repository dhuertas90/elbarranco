import pygame
from pygame.locals import *
import random
import time
import sys
import Mod_bot
import Mod_jue
import Mod_pj
import Mod_ran


def calcularpuntaje(op, cuentas, nivel):

    agreg = 2
    if cuentas <= 6:
        if op == '-':
            agreg = 5
        points = 2*nivel + agreg
    else:
        agreg = 1
        if op == '-':
            agreg = 3
        points = 1*nivel
    return points


def posbotones():

    lista = [250, 310, 370]
    p1 = random.randint(0, 2)
    if p1 == 0:
        p2 = random.randint(1, 2)
        if p2 == 1:
            p3 = 2
        else:
            p3 = 1
    elif p1 == 2:
        p2 = random.randint(0, 1)
        if p2 == 0:
            p3 = 1
        else:
            p3 = 0
    else:
        p2 = random.randint(0, 1)
        if p2 == 0:
            p3 = 2
        else:
            p2 = 2
            p3 = 0
    p1 = lista[p1]
    p2 = lista[p2]
    p3 = lista[p3]
    return p1, p2, p3


def imprimir(texto, x, y, pantalla, tam=20):

    fuente = pygame.font.Font("dejavu.ttf", tam)
    mensaje = fuente.render(texto, 1, (55, 55, 55))
    pantalla.blit(mensaje, (x, y))


def contador(num):

    if num < 5:
        num += 1
    elif num == 5:
        num = 0
    return num


def seleccionarFondo(niv):

    if niv <= 2:
        fondo = "fondojuego.png"
    elif niv > 2 and niv < 5:
        fondo = "fondojuego2.png"
    else:
        fondo = "fondojuego3.png"
    return fondo


def nuevojuego(pantalla, apodo, genero):

    pygame.display.set_caption('Jugando El Barranco..')
    cursor = Mod_bot.Cursor()
    nue = Mod_jue.Juego(genero)
    ran = Mod_ran.Ranking()
    win = False
    correctas = 0
    cuentas = 0
    sumas = 0
    restas = 0
    vidas = nue.get_vidas()
    nivel = nue.get_nivel()
    while (vidas > 0) and (win is False):

        vida = str(nue.get_vidas())
        niv = str(nue.get_nivel())
        puntos = str(nue.get_puntaje())
        # Load display
        fondoDelJuego = seleccionarFondo(int(niv))
        fondojuego = pygame.image.load(fondoDelJuego)
        fondotiempo = pygame.image.load("reloj1.png")
        fondojuego.blit(fondotiempo, (670, 8))
        pantalla.blit(fondojuego, (0, 0))
        imprimir(vida, 110, 18, pantalla)
        imprimir('Nivel  ' + niv, 194, 15, pantalla)
        imprimir('Puntos  ' + puntos, 317, 15, pantalla)
        pj = Mod_pj.Personaje(nue.get_genero(), fondoDelJuego)
        seconds = time.localtime().tm_sec
        mas60 = 60
        # posicion de los botones
        pos1, pos2, pos3 = posbotones()
        # obtengo el resultado de la cuenta y el operador a utilizar
        res, op = nue.cuenta(sumas, restas, cuentas, pantalla)
        # creacion de los botones
        pru = pygame.image.load("bot.png")
        pru2 = pygame.image.load("bot2.png")
        boton = Mod_bot.BotonNumero(pru, pru2, 620, pos1, res, pantalla)
        pru = pygame.image.load("bot.png")
        pru2 = pygame.image.load("bot2.png")
        boton1 = Mod_bot.BotonNumero(pru, pru2, 620, pos2, res + 5, pantalla)
        pru = pygame.image.load("bot.png")
        pru2 = pygame.image.load("bot2.png")
        boton2 = Mod_bot.BotonNumero(pru, pru2, 620, pos3, res - 5, pantalla)
        sonido = Mod_bot.BotonSonido(685, 450, pantalla)
        unsegundo = 0  # contador de 10 segundos (600ms)
        seg = 0
        clock = pygame.time.Clock()
        error = 2  # inicializo error por tiempo
        listo = False
        while (listo is False):
            # sin respuesta aun..
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    botones_mouse = pygame.mouse.get_pressed()
                    if botones_mouse[0] == 1:
                        if cursor.colliderect(boton.rect):
                            # Update score
                            puntos = calcularpuntaje(op, cuentas, nivel)
                            puntaje = nue.get_puntaje()
                            nue.set_puntaje(puntaje+puntos)
                            # End update score
                            error = 0  # Right answer
                            listo = True
                        elif cursor.colliderect(boton1.rect):
                            error = 1  # Wrong answer
                            listo = True
                        elif cursor.colliderect(boton2.rect):
                            error = 1  # Wrong answer
                            listo = True
                        elif cursor.colliderect(sonido.rect):
                            sonido.swich(sonidos, pantalla)
                        else:
                            pass

                cursor.update()
                boton.updateNumero(pantalla, cursor)
                boton1.updateNumero(pantalla, cursor)
                boton2.updateNumero(pantalla, cursor)
            pygame.display.flip()
            # contador de segundos
            if time.localtime().tm_sec != seconds:
                unsegundo += 1
                if unsegundo == mas60:
                    seg += 1
                    tex = str(seg)
                    pantalla.blit(fondotiempo, (670, 8))
                    pygame.display.update()
                    imprimir(tex, 685, 20, pantalla, tam=25)
                    mas60 += 60
                if unsegundo == 960:
                    # 10 segundos
                    listo = True
        pj.Caminar(2, pantalla)
        if error == 0:
            # respuesta correcta
            if op == '+':
                sumas += 1
            else:
                restas += 1
            correctas += 1
            pj.Saltar(pantalla)
        else:
            # respuesta incorrecta
            nue.set_vidas(vidas - 1)
            vidas = vidas - 1
            pj.Caer(pantalla)
        cuentas += 1  # cantidad de cuentas mostradas durante el juego
        # analizar nivel actual
        if correctas == 6 and nivel < 5:
            nue.set_nivel(nivel + 1)  # actualizar nivel
            nivel += 1
            sumas = 0
            restas = 0
            correctas = 0
            cuentas = 0
        elif correctas == 6 and nivel == 5:
            win = True
            break
    ran.set_tabla(nue.get_puntaje(), apodo)
    if (win is True):
        fondoganador = pygame.image.load("ganador.png")
        imprimir('G A N A S T E !', 290, 300, fondoganador, tam=25)
        imprimir(str(nue.get_puntaje()) + ' puntos', 290,
                 350, fondoganador, tam=25)
        pantalla.blit(fondoganador, (0, 0))
        pygame.display.flip()
        pygame.time.delay(5000)
    else:
        fondogameover = pygame.image.load("gameover.png")
        fondogameover1 = pygame.image.load("gameover1.png")
        for i in range(0, 50):
            pantalla.blit(fondogameover, (0, 0))
            pygame.display.flip()
            pygame.time.delay(100)
            pantalla.blit(fondogameover1, (0, 0))
            pygame.display.flip()
            pygame.time.delay(100)
        pygame.time.delay(500)
