import pygame
import Mod_bot
import Mod_fun


def cont(num):

    if num < 2:
        num += 1
    elif num == 2:
        num = 0
    return num


def ayuda(pantalla):

    atras = pygame.image.load("flecha.png")
    atras1 = pygame.image.load("flecha1.png")
    boton = Mod_bot.Boton(atras1, atras, 10, 440)
    adelante = pygame.image.load("adelante.png")
    adelante1 = pygame.image.load("adelante1.png")
    botAdelante = Mod_bot.Boton(adelante, adelante1, 660, 440)
    cursor = Mod_bot.Cursor()
    pygame.display.set_caption(' Ayuda ')
    sonido = pygame.mixer.Sound('ayud.wav')
    sonido.set_volume(0.3)
    sonido.play(loops=(-1))
    img1 = pygame.image.load("fondoAyuda2.png")
    img2 = pygame.image.load("fondoAyuda3.png")
    img3 = pygame.image.load("fondoAyuda4.png")
    lista = [img1, img2, img3]
    fondoayuda = lista[0]
    num = 0
    salir = False
    while salir is False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                botones_mouse = pygame.mouse.get_pressed()
                if botones_mouse[0] == 1:
                    if cursor.colliderect(boton.rect):
                        if fondoayuda == img1:
                            salir = True
                        else:
                            if num > 0:
                                num -= 1
                        fondoayuda = lista[num]
                    elif cursor.colliderect(botAdelante.rect):
                        if num < 2:
                            num += 1
                        fondoayuda = lista[num]
        pantalla.blit(fondoayuda, (0, 0))
        cursor.update()
        boton.update(pantalla, cursor)
        if num != 2:
            botAdelante.update(pantalla, cursor)
        pygame.display.flip()
    sonido.stop()
    pygame.display.set_caption("MENU - EL BARRANCO")
