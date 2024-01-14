import pygame
import sys
from pygame.locals import *
sys.path.append("./modules/")
import Mod_bot as bot


letras_permitidas = {
    K_a: 'a', K_b: 'b', K_c: 'c', K_d: 'd', K_e: 'e', K_f: 'f', K_g: 'g', K_h: 'h', K_i: 'i',
    K_j: 'j', K_k: 'k', K_l: 'l', K_m: 'm', K_n: 'n', K_o: 'o', K_p: 'p', K_q: 'q', K_r: 'r', K_s: 's',
    K_t: 't', K_u: 'u', K_v: 'v', K_w: 'w', K_x: 'x', K_y: 'y', K_z: 'z'
    }

def mostrar(pantalla, fondo, key, pos, pos2=220, tam=50, c=(255, 255, 255)):
    fuente = pygame.font.Font("data/Cascadia.ttf", tam)
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
    varon_selected = nena_selected = 0
    salir = True
    datos = ''
    while salir:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.mixer.music.stop()
                salir = True
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if maximo > cant:
                    if event.key in letras_permitidas:
                        letra = letras_permitidas[event.key]
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
                        varon_selected += 1
                        if varon_selected > 1:
                            ok = False
                            varon_selected = 0
                        else:
                            ok = True
                        print(ok, varon_selected)
                    elif cursor.colliderect(b_nena.rect):
                        b_nena.swich(pantalla, fondo)
                        genero = 'nena'
                        b_varon = bot.BotonOK(var, 550, 150, pantalla, fondo)
                        nena_selected += 1
                        print(f"nena_selected --> {nena_selected}")
                        if nena_selected > 1:
                            ok = False
                            nena_selected = 0
                        else:
                            ok = True
                    elif cursor.colliderect(b_borrar.rect):
                        datos = ('borrar', 'borrar') 
                        salir = True
                        return datos
                    elif cursor.colliderect(b_enter.rect):
                        print(f"OK es --> {ok}")
                        if ok and (apodo != ''):
                            datos = (apodo, genero)
                            salir = True
                            return datos
                        else:
                            msj = "INGRESE NOMBRE Y SELECCIONE PERSONAJE!"
                            mostrar(pantalla, fondo, msj, 10, pos2=10, tam=30, c=(0, 0, 0))
                            pygame.time.delay(500)
                    elif cursor.colliderect(boton.rect):
                        datos = ('exit', 'exit') 
                        salir = True
                        return datos
                    else:
                        pass
        pantalla.blit(fondo, (0, 0))
        cursor.update()
        b_borrar.update(pantalla, cursor)
        b_enter.update(pantalla, cursor)
        boton.update(pantalla, cursor)
        pygame.display.flip()
    