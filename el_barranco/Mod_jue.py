import pygame
import random


class Juego():
    def __init__(self, var, estado=False):
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

    def set_nivel(self, actual):
        self.nivel = actual

    def set_vidas(self, actual):
        self.vidas = actual

    def set_puntaje(self, actual):
        self.puntaje = actual

    def set_genero(self, actual):
        self.genero = actual

    def calcular_operador(self, cr, cs, cant):
        """Se selecciona el operando del calculo a resolver, dependiendo del criterio en base al nivel
        que se encuentra el juego"""
        if cant < 6:  # Intercalar operadores
            op = '+' if cant % 2 == 0 else '-'
        else:  # Operador depende de cantidad sumas y restas
            if cs < 3 and cr < 3:
                op = '+' if cant % 2 == 0 else '-'
            elif cr == 3 and cs < 3:
                op = '+'
            else:
                op = '-'
        return op

    def cargar_cuenta(self, level):
        """Carga los valores de los operandos para armar la cuenta"""
        if level == 1:
            v1, v2 = random.randint(2, 9), random.randint(1, 5)
        elif level == 2:
            v1, v2 = random.randint(10, 50), random.randint(2, 9)
        elif level == 3:
            v1, v2 = random.randint(50, 70), random.randint(10, 15)
        elif level == 4:
            v1, v2 = random.randint(70, 100), random.randint(15, 50)
        else:
            v1, v2 = random.randint(100, 1000), random.randint(50, 100)
        return v1, v2

    def cuenta(self, sumas, restas, cant, pantalla):
        """Se trabaja con la suma y se elige un operando que puede ser suma o resta.
        En caso de ser resta, el calculo se convierte en sustraccion al sumar un numero positivo con uno negativo
        Operación: num1 + (- num2)
        Se convierte en la operación: num1 - num2"""
        # obtengo el nivel actual
        level = self.get_nivel()
        # obtengo valores de la suma a crear
        v1, v2 = self.cargar_cuenta(level)
        op = self.calcular_operador(restas, sumas, cant)
        # obtengo suma y evaluo su operando
        suma = eval(str(v1)+op+str(v2))
        fuente = pygame.font.Font("data/dejavu.ttf", 20)
        texto = "Calcular:  %d %s %d = " % (v1, op, v2)
        mensaje = fuente.render(texto, 1, (255, 255, 255))
        pantalla.blit(mensaje, (15, 290)) 
        # "suma" representa la adicion de un numero positivo con un numero positivo/negativo
        return suma, op 
