import pygame
import sys, time
from pygame.locals import *
sys.path.append("./modules/")
import Mod_bot as bot


def mostrar(pantalla, fondo, key, pos, pos2=220, tam=50, c=(255, 255, 255)):
    fuente = pygame.font.Font("data/dejavu.ttf", tam)
    letra = fuente.render(key, 1, c)
    fondo.blit(letra, (pos, pos2))
    pantalla.blit(fondo, (0, 0))
    pygame.display.flip()

def ingresenombre(cursor, pantalla):
    # Pantalla antesala a comenzar a jugar
    pygame.display.set_caption('EL BARRANCO')
    fondo = pygame.image.load("data/fondoNombre.png")
    enter, enter2 = pygame.image.load("data/jugar.png"), pygame.image.load("data/jugar1.png")
    b_enter = bot.Boton(enter, enter2, 250, 300)
    borrar, borrar2 = pygame.image.load("data/borrar.png"), pygame.image.load("data/borrar1.png")
    b_borrar = bot.Boton(borrar, borrar2, 20, 300)
    var, nen = pygame.image.load("data/cuadrado1.png"), pygame.image.load("data/cuadrado.png")
    b_varon = bot.BotonOK(var, 550, 150, pantalla, fondo)
    b_nena = bot.BotonOK(nen, 550, 310, pantalla, fondo)
    atras, atras1 = pygame.image.load("data/flecha.png"), pygame.image.load("data/flecha1.png")
    boton = bot.Boton(atras1, atras, 10, 440)
    imgvaron, imgnena = pygame.image.load("data/varon.png"), pygame.image.load("data/nena.png")
    fondo.blit(imgvaron, (630, 100))
    fondo.blit(imgnena, (630, 300))
    ok, apodo, maximo, cant, pos = False, '', 8, 0, 165
    var_selected = nen_selected = 0
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
                    if cursor.colliderect(b_varon.rect):
                        b_varon.swich(pantalla, fondo)
                        genero = 'varon'
                        b_nena = bot.BotonOK(var, 550, 310, pantalla, fondo)
                        var_selected += 1
                        if var_selected > 1:
                            ok = False
                            var_selected = 0
                        else:
                            ok = True
                    elif cursor.colliderect(b_nena.rect):
                        b_nena.swich(pantalla, fondo)
                        genero = 'nena'
                        b_varon = bot.BotonOK(var, 550, 150, pantalla, fondo)
                        nen_selected += 1
                        if nen_selected > 1:
                            ok = False
                            nen_selected = 0
                        else:
                            ok = True
                    elif cursor.colliderect(b_borrar.rect):
                        return ('borrar', 'borrar')
                        salir = True
                        break
                    elif cursor.colliderect(b_enter.rect):
                        if ok and (apodo != ''):
                            return (apodo, genero)
                            salir = True
                            break
                        else:
                            msj = "INGRESE NOMBRE Y SELECCIONE PERSONAJE!"
                            mostrar(pantalla, fondo, msj, 10, pos2=10, tam=30, c=(0, 0, 0))
                            pygame.time.delay(500)
                    elif cursor.colliderect(boton.rect):
                        return ('exit', 'exit')
                        salir = True
                        break
                    else:
                        pass
        pantalla.blit(fondo, (0, 0))
        cursor.update()
        b_borrar.update(pantalla, cursor)
        b_enter.update(pantalla, cursor)
        boton.update(pantalla, cursor)
        pygame.display.flip()
