import pygame
import random
import Mod_pj


class Juego():

    def __init__(self, var):

        self.nivel = 1
        self.puntaje = 0
        self.vidas = 10
        self.genero = var

    def get_puntaje(self):

        return self.puntaje

    def get_vidas(self):

        return self.vidas

    def get_nivel(self):

        return self.nivel

    def get_genero(self):

        return self.genero

    def set_nivel(self, actualn):

        self.nivel = actualn

    def set_vidas(self, actualv):

        self.vidas = actualv

    def set_puntaje(self, actualp):

        self.puntaje = actualp

    def set_genero(self, actualg):

        self.genero = actualg

    def calcularoperador(self, cr, cs, cant):

        if cant < 6:  # significa que hay que intercalar
            if cant % 2 == 0:
                op = '+'
            else:
                op = '-'
        else:  # operador depende de cantidad sumas y restas
            if cs < 3 and cr < 3:
                if cant % 2 == 0:
                    op = '+'
                else:
                    op = '-'
            elif cr == 3 and cs < 3:
                op = '+'
            else:
                op = '-'
        return op

    def cargarcuenta(self, level):

        if level == 1:
            v1 = random.randint(2, 9)
            v2 = random.randint(1, 5)
        elif level == 2:
            v1 = random.randint(10, 50)
            v2 = random.randint(2, 9)
        elif level == 3:
            v1 = random.randint(50, 70)
            v2 = random.randint(10, 15)
        elif level == 4:
            v1 = random.randint(70, 100)
            v2 = random.randint(15, 50)
        else:
            v1 = random.randint(100, 1000)
            v2 = random.randint(50, 100)
        return v1, v2

    def cuenta(self, sumas, restas, cant, pantalla):

        level = self.get_nivel()  # obtengo el nivel actual
        v1, v2 = self.cargarcuenta(level)  # obtengo valores de la suma a crear
        op = self.calcularoperador(restas, sumas, cant)
        suma = eval(str(v1)+op+str(v2))  # obtengo suma(principal)
        fuente = pygame.font.Font("dejavu.ttf", 20)
        texto = "Calcular:  %d %s %d = " % (v1, op, v2)
        mensaje = fuente.render(texto, 1, (255, 255, 255))
        pantalla.blit(mensaje, (15, 290))
        # muestro mensaje en pantalla(suma)
        return suma, op  # devuelvo el dato suma
