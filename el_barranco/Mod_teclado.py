import pygame
import sys
import time
from pygame.locals import *
import Mod_bot


def mostrar(pantalla, fondo, key, pos, pos2=220, tam=50, c=(255, 255, 255)):

    fuente = pygame.font.Font("dejavu.ttf", tam)
    letra = fuente.render(key, 1, c)
    fondo.blit(letra, (pos, pos2))
    pantalla.blit(fondo, (0, 0))
    pygame.display.flip()


def ingresenombre(cursor, pantalla):

    pygame.display.set_caption('EL BARRANCO')
    fondo = pygame.image.load("fondoNombre.png")
    enter = pygame.image.load("jugar.png")
    enter2 = pygame.image.load("jugar1.png")
    botonE = Mod_bot.Boton(enter, enter2, 250, 300)
    borrar = pygame.image.load("borrar.png")
    borrar2 = pygame.image.load("borrar1.png")
    botonB = Mod_bot.Boton(borrar, borrar2, 100, 300)
    var = pygame.image.load("cuadrado1.png")
    bot_var = Mod_bot.BotonOK(var, 500, 200, pantalla, fondo)
    nen = pygame.image.load("cuadrado.png")
    bot_nen = Mod_bot.BotonOK(nen, 500, 350, pantalla, fondo)
    atras = pygame.image.load("flecha.png")
    atras1 = pygame.image.load("flecha1.png")
    boton = Mod_bot.Boton(atras1, atras, 10, 440)
    imgvaron = pygame.image.load("varon.png")
    fondo.blit(imgvaron, (550, 150))
    imgnena = pygame.image.load("nena.png")
    fondo.blit(imgnena, (550, 300))
    ok = False
    apodo = ''
    maximo = 8
    cant = 0
    pos = 27
    salir = True
    while (salir is True):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.mixer.music.stop()
                salir = True
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if maximo > cant:
                    if event.key == K_a:
                        letra = 'a'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_b:
                        letra = 'b'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_c:
                        letra = 'c'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_d:
                        letra = 'd'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 35
                        cant += 1
                    elif event.key == K_e:
                        letra = 'e'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 30
                        cant += 1
                    elif event.key == K_f:
                        letra = 'f'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 30
                        cant += 1
                    elif event.key == K_g:
                        letra = 'g'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_h:
                        letra = 'h'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_i:
                        letra = 'i'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 20
                        cant += 1
                    elif event.key == K_j:
                        letra = 'j'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_k:
                        letra = 'k'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_l:
                        letra = 'l'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 30
                        cant += 1
                    elif event.key == K_m:
                        letra = 'm'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 45
                        cant += 1
                    elif event.key == K_n:
                        letra = 'n'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 35
                        cant += 1
                    elif event.key == K_o:
                        letra = 'o'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_p:
                        letra = 'p'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 35
                        cant += 1
                    elif event.key == K_q:
                        letra = 'q'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_r:
                        letra = 'r'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_s:
                        letra = 's'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 35
                        cant += 1
                    elif event.key == K_t:
                        letra = 't'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_u:
                        letra = 'u'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_v:
                        letra = 'v'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_w:
                        letra = 'w'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 45
                        cant += 1
                    elif event.key == K_x:
                        letra = 'x'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_y:
                        letra = 'y'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 40
                        cant += 1
                    elif event.key == K_z:
                        letra = 'z'
                        mostrar(pantalla, fondo, letra, pos)
                        pos += 35
                        cant += 1
                    else:
                        letra = ''
                apodo += letra
            if event.type == pygame.MOUSEBUTTONDOWN:
                botones_mouse = pygame.mouse.get_pressed()
                if botones_mouse[0] == 1:
                    if cursor.colliderect(bot_var.rect):
                        bot_var.swich(pantalla, fondo)
                        genero = 'varon'
                        bot_nen = Mod_bot.BotonOK(nen, 500, 350,
                                                  pantalla, fondo)
                        ok = True
                    elif cursor.colliderect(bot_nen.rect):
                        bot_nen.swich(pantalla, fondo)
                        genero = 'nena'
                        bot_var = Mod_bot.BotonOK(var, 500, 200,
                                                  pantalla, fondo)
                        ok = True
                    elif cursor.colliderect(botonB.rect):
                        return ('borrar', 'borrar')
                        salir = True
                        break
                    elif cursor.colliderect(botonE.rect):
                        if ok and (apodo != ''):
                            return (apodo, genero)
                            salir = True
                            break
                        else:
                            msj = "INGRESE NOMBRE Y SELECCIONE PERSONAJE!"
                            mostrar(pantalla, fondo, msj, 10, pos2=10,
                                    tam=30, c=(0, 0, 0))
                            pygame.time.delay(500)
                    elif cursor.colliderect(boton.rect):
                        return ('exit', 'exit')
                        salir = True
                        break
                    else:
                        pass
        pantalla.blit(fondo, (0, 0))
        cursor.update()
        botonB.update(pantalla, cursor)
        botonE.update(pantalla, cursor)
        boton.update(pantalla, cursor)
        pygame.display.flip()
