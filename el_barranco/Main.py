import pygame
import pickle
import os, sys
import time
import modules.Mod_ran as ran, modules.Mod_ayuda as ayu, modules.Mod_fun as fun, modules.Mod_bot as bot, modules.Mod_teclado as tec
from pygame.locals import *


pantalla_ancho = 730
pantalla_alto = 500
sonidos = []
ancho_x = 270
alto_y = 250
dist = 40
long = 90


# Posicion Botones del Menu
nuevo_y = alto_y
ranking_y = alto_y + dist
ayuda_y = alto_y + (dist*2)
salir_y = alto_y + (dist*3)

def cargar_botones():
    """Inicializacion Botones del Menu"""
    juego, juego1 = pygame.image.load("data/nuevojuego.png"), pygame.image.load("data/nuevojuego1.png")
    boton_1 = bot.Boton(juego, juego1, ancho_x, nuevo_y)
    ranking, ranking1 = pygame.image.load("data/ranking.png"), pygame.image.load("data/ranking1.png")
    boton_2 = bot.Boton(ranking, ranking1, ancho_x, ranking_y)
    opciones, opciones1 = pygame.image.load("data/ayuda1.png"), pygame.image.load("data/ayuda.png")
    boton_3 = bot.Boton(opciones, opciones1, ancho_x, ayuda_y)
    salir, salir1 = pygame.image.load("data/salir.png"), pygame.image.load("data/salir1.png")
    boton_4 = bot.Boton(salir, salir1, ancho_x, salir_y)
    return boton_1, boton_2, boton_3, boton_4

def cargar_sonidos():
    sonidos.append(pygame.mixer.Sound('data/menu.wav'))
    sonidos.append(pygame.mixer.Sound('data/juego.wav'))
    sonidos.append(1) # Muted

def cambiar_sonidos(i, j):
    """Detiene sonido i, hace sonar sonido j"""
    sonidos[i].stop()
    sonidos[j].play(loops=-1)

def main():
    cargar_sonidos()
    pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
    fondo = pygame.image.load("data/fondo.png")
    pygame.display.set_caption("MENU - EL BARRANCO")
    rank = ran.Ranking()
    cursor = bot.Cursor()

    boton_1, boton_2, boton_3, boton_4 = cargar_botones()
    salir = False
    sonidos[0].play(loops=-1)  # PLAY SONIDO MENU

    while (not salir):
        borrar = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                salir = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                botones_mouse = pygame.mouse.get_pressed()
                if botones_mouse[0] == 1:
                    if cursor.colliderect(boton_1.rect):
                        cambiar_sonidos(0, 1)
                        while (not borrar):
                            tuplaPj = tec.ingresenombre(cursor, pantalla)
                            borrar = False if tuplaPj[0] == 'borrar' else True
                        if tuplaPj[0] == 'exit':
                            cambiar_sonidos(1,0)
                            break
                        fun.nuevo_juego(pantalla, sonidos, tuplaPj[0], tuplaPj[1])
                        cambiar_sonidos(1,0)
                        rank.get_ranking(sonidos, pantalla)
                    if cursor.colliderect(boton_2.rect):
                        rank.get_ranking(sonidos, pantalla)
                    if cursor.colliderect(boton_3.rect):
                        sonidos[0].stop()
                        ayu.ayuda(pantalla)
                        sonidos[1].play(loops=-1)
                    if cursor.colliderect(boton_4.rect):
                        salir = True
                        pygame.quit()
                        sys.exit()
        pantalla.blit(fondo, (0, 0))
        cursor.update()
        boton_1.update(pantalla, cursor)
        boton_2.update(pantalla, cursor)
        boton_3.update(pantalla, cursor)
        boton_4.update(pantalla, cursor)
        pygame.display.flip()
    sonidos[0].stop()
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
