import pygame
import sys
sys.path.append("./modules/")
import archivo as arc
import Mod_bot as bot


class Ranking():
    def __init__(self):
        self.cantidad = 0
        self.maximo = 10

    def get_maximo(self):
        return self.maximo
    
    def get_ranking(self, sonidos, pantalla):
        try:
            lista = arc.desarchivar('data/ranking.txt')
        except IOError:
            f = open('data/ranking.txt', 'w')
            f.close()
            lista = [['(vacio)', '0']]
            lista = lista * self.get_maximo()
        sonidos[0].play(loops=-1)  # SONIDO RANKING REPITIENDOSE
        atras, atras1 = pygame.image.load("data/flecha.png"), pygame.image.load("data/flecha1.png")
        boton, cursor = bot.Boton(atras1, atras, 10, 440), bot.Cursor()
        pygame.display.set_caption(' Ranking ')
        fondoranking = pygame.image.load("data/fondorank.png")
        pos = 220
        fuente = pygame.font.Font("data/dejavu.ttf", 23)
        # Mostrar los mejores puntajes
        posicion = 1
        for puesto in lista:
            nom = puesto[0]
            pun = int(puesto[1])
            nombre = fuente.render(str(posicion)+' - '+nom, 1, (45, 45, 45))
            fondoranking.blit(nombre, (100, pos))
            puntaje = fuente.render(str(pun), 1, (45, 45, 45))
            fondoranking.blit(puntaje, (500, pos))
            posicion += 1
            pos += 23
        arc.archivar(lista, 'data/ranking.txt')
        salir = False
        while (salir is False):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    botones_mouse = pygame.mouse.get_pressed()
                    if botones_mouse[0] == 1:
                        if cursor.colliderect(boton.rect):
                            salir = True
            pantalla.blit(fondoranking, (0, 0))
            cursor.update()
            boton.update(pantalla, cursor)
            pygame.display.flip()
        pygame.display.set_caption('MENU - EL BARRANCO')
