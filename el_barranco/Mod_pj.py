import pygame
import time
import sys
sys.path.append("./modules/")
import Mod_fun as fun


class Personaje(pygame.sprite.Sprite):
    def __init__(self, genero, fondo):
        pygame.sprite.Sprite.__init__(self)
        self.listaImg = self.obtener_imagenes(genero)
        self.fondo = pygame.image.load(fondo)
        self.rect = self.listaImg[0].get_rect()
        self.rect.top = 110
        self.rect.left = 0

    def Caminar(self, vel, pantalla):
        num = 0
        num2 = 0
        for i in range(0, 140):
            self.rect.left += vel
            pantalla.blit(self.fondo, (0, 0))
            pantalla.blit(self.listaImg[num], self.rect)
            if num2 == 5:
                num = fun.contador(num)
            num2 = fun.contador(num2)
            pygame.display.update()

    def Golpe(self, pantalla):
        img1, img2 = pygame.image.load('data/golpe2.png'), pygame.image.load('data/golpe1.png')
        for i in range(0, 5):
            if i == 1:
                pantalla.blit(img1, (270, 423))
            if i == 4:
                pantalla.blit(img2, (335, 423))
        pygame.display.update()
        pygame.time.delay(200)

    def Caer(self, pantalla):
        for i in range(1, 7):
            self.rect.top -= i
            self.rect.left += i
            pantalla.blit(self.fondo, (0, 0))
            pantalla.blit(self.listaImg[2], self.rect)
            pygame.display.update()
        for i in range(1, 7):
            self.rect.top += i
            self.rect.left += i
            pantalla.blit(self.fondo, (0, 0))
            pantalla.blit(self.listaImg[2], self.rect)
            pygame.display.update()
        while self.rect.top < 500:
            self.rect.top += 1+5
            pantalla.blit(self.fondo, (0, 0))
            pantalla.blit(self.listaImg[4], self.rect)
            pygame.display.update()
        self.Golpe(pantalla)

    def Saltar(self, pantalla):
        for i in range(1, 15):
            self.rect.top -= i
            self.rect.left += i
            pantalla.blit(self.fondo, (0, 0))
            pantalla.blit(self.listaImg[2], self.rect)
            pygame.display.update()
        for i in range(1, 15):
            self.rect.top += i*1
            self.rect.left += i
            pantalla.blit(self.fondo, (0, 0))
            pantalla.blit(self.listaImg[3], self.rect)
            pygame.display.update()
        self.Caminar(4, pantalla)

    def obtener_imagenes(self, gen):
        if gen == 'varon':
            img1 = pygame.image.load("data/pj1.png")
            img2 = pygame.image.load("data/pj2.png")
            img3 = pygame.image.load("data/pj3.png")
            img4 = pygame.image.load("data/pj4.png")
            img5 = pygame.image.load("data/pj5.png")
            img6 = pygame.image.load("data/pj6.png")
        else:
            img1 = pygame.image.load("data/pjm1.png")
            img2 = pygame.image.load("data/pjm2.png")
            img3 = pygame.image.load("data/pjm3.png")
            img4 = pygame.image.load("data/pjm4.png")
            img5 = pygame.image.load("data/pjm5.png")
            img6 = pygame.image.load("data/pjm6.png")
        lista = [img1, img2, img3, img4, img5, img6]
        return lista
