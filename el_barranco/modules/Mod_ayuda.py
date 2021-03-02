import pygame
import sys
sys.path.append("./modules/")
import Mod_bot as bot


def cont(num):
    
    if num < 2:
        num += 1
    elif num == 2:
        num = 0
    return num


def ayuda(pantalla):

    atras = pygame.image.load("data/flecha.png")
    atras1 = pygame.image.load("data/flecha1.png")
    boton = bot.Boton(atras1, atras, 10, 440)
    adelante = pygame.image.load("data/adelante.png")
    adelante1 = pygame.image.load("data/adelante1.png")
    bot_adelante = bot.Boton(adelante, adelante1, 660, 440)
    cursor = bot.Cursor()
    pygame.display.set_caption(' Ayuda ')
    sonido = pygame.mixer.Sound('data/ayud.wav')
    sonido.set_volume(0.3)
    sonido.play(loops=(-1))
    img1 = pygame.image.load("data/fondoAyuda2.png")
    img2 = pygame.image.load("data/fondoAyuda3.png")
    img3 = pygame.image.load("data/fondoAyuda4.png")
    lista = [img1, img2, img3]
    fondo_ayuda = lista[0]
    num = 0
    salir = False
    while salir is False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                botones_mouse = pygame.mouse.get_pressed()
                if botones_mouse[0] == 1:
                    if cursor.colliderect(boton.rect):
                        if fondo_ayuda == img1:
                            salir = True
                        else:
                            if num > 0:
                                num -= 1
                        fondo_ayuda = lista[num]
                    elif cursor.colliderect(bot_adelante.rect):
                        if num < 2:
                            num += 1
                        fondo_ayuda = lista[num]
        pantalla.blit(fondo_ayuda, (0, 0))
        cursor.update()
        boton.update(pantalla, cursor)
        if num != 2:
            bot_adelante.update(pantalla, cursor)
        pygame.display.flip()
    sonido.stop()
    pygame.display.set_caption("MENU - EL BARRANCO")
