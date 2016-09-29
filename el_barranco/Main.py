import pygame
import pickle
import os
import sys
import time
import Mod_ran
import Mod_ayuda
import Mod_fun
import Mod_bot
import Mod_teclado
from pygame.locals import *


def main():

    # beginning to load sounds
    sonidos = []
    sonidos.append(pygame.mixer.Sound('menu.wav'))
    sonidos.append(pygame.mixer.Sound('juego.wav'))
    pantalla = pygame.display.set_mode((730, 500))
    # ending to load sounds.
    fondo = pygame.image.load("fondo.png")
    pygame.display.set_caption("MENU - EL BARRANCO")
    rank = Mod_ran.Ranking()
    cursor = Mod_bot.Cursor()
    # 3 variables to positioning
    x = 270
    y = 250
    dist = 40
    # beginning to load images
    juego = pygame.image.load("nuevojuego.png")
    juego1 = pygame.image.load("nuevojuego1.png")
    boton1 = Mod_bot.Boton(juego, juego1, x, y)
    ranking = pygame.image.load("ranking.png")
    ranking1 = pygame.image.load("ranking1.png")
    boton2 = Mod_bot.Boton(ranking, ranking1, x, y=y+dist)
    opciones = pygame.image.load("ayuda1.png")
    opciones1 = pygame.image.load("ayuda.png")
    boton3 = Mod_bot.Boton(opciones, opciones1, x, y=y+dist+dist)
    salir = pygame.image.load("salir.png")
    salir1 = pygame.image.load("salir1.png")
    boton4 = Mod_bot.Boton(salir, salir1, x, y=y+dist+dist+dist)
    # ending to load images.
    salir = False  # Boolean, end program.
    sonidos[0].play(loops=-1)  # SONIDO MENU REPITIENDOSE
    while (salir is False):
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
                    if cursor.colliderect(boton1.rect):
                        sonidos[0].stop()  # STOP SONIDO MENU
                        sonidos[1].play(loops=-1)  # SONIDO JUEGO REPETIENDOSE
                        while (borrar is False):
                            tuplaPj = Mod_teclado.ingresenombre(cursor,
                                                                pantalla)
                            if tuplaPj[0] == 'borrar':
                                borrar = False
                            else:
                                borrar = True  # no aprete Borrar (medio raro)
                        if tuplaPj[0] == 'exit':
                            sonidos[1].stop()
                            sonidos[0].play(loops=-1)
                            break
                        Mod_fun.nuevojuego(pantalla, tuplaPj[0], tuplaPj[1])
                        sonidos[1].stop()
                        sonidos[0].play(loops=-1)
                        rank.get_ranking(sonidos, pantalla)
                    if cursor.colliderect(boton2.rect):
                        rank.get_ranking(sonidos, pantalla)
                    if cursor.colliderect(boton3.rect):
                        sonidos[0].stop()
                        Mod_ayuda.ayuda(pantalla)
                        sonidos[1].play(loops=-1)
                    if cursor.colliderect(boton4.rect):
                        salir = True
                        pygame.quit()
                        sys.exit()
        pantalla.blit(fondo, (0, 0))
        cursor.update()
        boton1.update(pantalla, cursor)
        boton2.update(pantalla, cursor)
        boton3.update(pantalla, cursor)
        boton4.update(pantalla, cursor)
        pygame.display.flip()
    sonidos[0].stop()
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    main()
