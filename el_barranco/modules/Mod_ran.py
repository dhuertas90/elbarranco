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
    
    def cargar_imagen(self, ruta):
        return pygame.image.load(ruta)
    
    def configurar_botones(self):
        atras, atras1 = self.cargar_imagen("data/flecha.png"), self.cargar_imagen("data/flecha1.png")
        return bot.Boton(atras1, atras, 10, 440), bot.Cursor()

    def mostrar_mejores_puntajes(self, lista, fondo, fuente):
        # Mostrar los mejores puntajes
        pos = 220
        posicion = 1
        for puesto in lista:
            nom = puesto[0]
            pun = int(puesto[1])
            nombre = fuente.render(str(posicion)+' - '+nom, 1, (45, 45, 45))
            fondo.blit(nombre, (100, pos))
            puntaje = fuente.render(str(pun), 1, (45, 45, 45))
            fondo.blit(puntaje, (500, pos))
            posicion += 1
            pos += 23

    def guardar_ranking(self, lista):
        arc.archivar(lista, 'data/ranking.txt')

    def bucle_escuchador(self, pantalla, fondo, cursor, boton):
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    botones_mouse = pygame.mouse.get_pressed()
                    if botones_mouse[0] == 1:
                        if cursor.colliderect(boton.rect):
                            salir = True
            pantalla.blit(fondo, (0, 0))
            cursor.update()
            boton.update(pantalla, cursor)
            pygame.display.flip()

    def get_ranking(self, sonidos, pantalla):
        try:
            lista = arc.desarchivar('data/ranking.txt')
        except IOError:
            f = open('data/ranking.txt', 'w')
            f.close()
            lista = [['(vacio)', '0']]
            lista = lista * self.get_maximo()
        sonidos[0].play(loops=-1)  # SONIDO RANKING REPITIENDOSE
        boton, cursor = self.configurar_botones()
        pygame.display.set_caption(' Ranking ')
        fondoranking = self.cargar_imagen("data/fondorank.png")
        fuente = pygame.font.Font("data/dejavu.ttf", 23)
        # Mostrar los mejores puntajes
        self.mostrar_mejores_puntajes(lista, fondoranking, fuente)
        self.guardar_ranking(lista)
        self.bucle_escuchador(pantalla, fondoranking, cursor, boton)
        
        pygame.display.set_caption('MENU - EL BARRANCO')

    def add_to_ranking(self, puntaje, apodo):
        try:
            lista = arc.desarchivar('data/ranking.txt')
        except IOError:
            lista = [['(vacio)', '0']]
            lista = lista * self.get_maximo()

        # Agregar el nuevo puntaje y apodo a la lista
        lista.append([apodo, str(puntaje)])

        # Ordenar la lista por puntajes de mayor a menor
        lista.sort(key=lambda x: int(x[1]), reverse=True)

        # Limitar la lista a un número máximo de elementos (si es necesario)
        lista = lista[:self.get_maximo()]

        # Archivar la lista actualizada de nuevo al archivo
        arc.archivar(lista, 'data/ranking.txt')