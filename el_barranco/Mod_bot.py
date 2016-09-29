import pygame


class Cursor(pygame.Rect):

    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()


class Boton(pygame.sprite.Sprite):

    def __init__(self, imagen1, imagen2, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.sonido = pygame.mixer.Sound('boton.wav')
        self.sonido.set_volume(0.1)

    def update(self, pantalla, cursor):
        num = 0
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
            if num != 1:
                self.sonido.play(0, 0, 1)
                num = 1
        else:
            self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual, self.rect)


class BotonNumero(pygame.sprite.Sprite):

    def __init__(self, imagen1, imagen2, x, y, numero, pantalla):

        pygame.sprite.Sprite.__init__(self)
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.texto = str(numero)
        self.fuente = pygame.font.Font("dejavu.ttf", 16)
        self.mensaje = self.fuente.render(self.texto, True, (255, 255, 255))
        self.imagen_actual.blit(self.mensaje,
                                (self.rect.centerx-13, self.rect.centery-13))
        self.imagen_seleccion.blit(self.mensaje,
                                  (self.rect.centerx-13, self.rect.centery-13))
        self.rect.left, self.rect.top = (x, y)
        self.sonido = pygame.mixer.Sound('boton.wav')
        self.sonido.set_volume(0.1)

    def updateNumero(self, pantalla, cursor):

        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
            self.sonido.play(0, 0, 1)
        else:
            self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual, self.rect)


class BotonSonido(pygame.sprite.Sprite):

    def __init__(self, x, y, pantalla):

        pygame.sprite.Sprite.__init__(self)
        self.imagenON = pygame.image.load("sonido.png")
        self.imagenOFF = pygame.image.load("sonido1.png")
        self.imag_act = self.imagenON
        self.rect = self.imag_act.get_rect()
        self.rect.left, self.rect.top = (x, y)
        pantalla.blit(self.imag_act, self.rect)

    def swich(self, sonidos, pantalla):

        if self.imag_act == self.imagenON:
            self.imag_act = self.imagenOFF
            sonidos[1].set_volume(0.0)
        else:
            self.imag_act = self.imagenON
            sonidos[1].set_volume(1.0)
        pantalla.blit(self.imag_act, self.rect)


class BotonOK (pygame.sprite.Sprite):

    def __init__(self, cuadro, x, y, pantalla, fondo):

        pygame.sprite.Sprite.__init__(self)
        self.imagen = cuadro
        self.imagenOk = pygame.image.load("ok.png")
        self.estado = False
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (x, y)
        fondo.blit(self.imagen, self.rect)
        pantalla.blit(fondo, (0, 0))

    def swich(self, pantalla, fondo):

        if self.estado is False:
            self.estado = True
            fondo.blit(self.imagenOk, self.rect)
            pantalla.blit(fondo, (0, 0))
        else:
            self.estado = False
            fondo.blit(self.imagen, self.rect)
            pantalla.blit(fondo, (0, 0))
