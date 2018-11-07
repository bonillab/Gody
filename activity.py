import pygame,sys
import random
from pygame.locals import *
from utils import CURSOR, img, font
import gtk

resolution=(1200,900)

class Main_Class():
    color = 163,231,240
    font_size = 50
    font_type = "Arial"

    def __init__(self):
        pygame.init()
        cursor = pygame.cursors.compile(CURSOR)
        pygame.mouse.set_cursor((32,32), (1,1), * cursor)
        self.ventana=pygame.display.set_mode((resolution))
        pygame.display.set_caption("Dinosaurio XD")
        self.principal()
        pygame.display.update()

    def image_load(self, path):
        return pygame.image.load(path)

    def ran(self, matriz):
        self.size = len(matriz)
        x = range(self.size)
        random.shuffle(x)
        return x

    def principal(self):
        self.pos_letter = 0
        self.dic = {}
        self.dic_letter = {}
        self.resp_font = []
        self.mt = self.ran(img)
        self.fondo = self.image_load('img/background.png')
        self.ventana.blit(self.fondo, (0, 0))
        self.load_img()
        self.load_font()
        self.detection_click()

    def load_img(self):
        try:
            x = 75
            self.resp = []
            for i in self.mt:
                image = self.image_load(img[i][0])
                rect = image.get_rect()
                rect.left = x
                rect.top = img[i][1]
                self.ventana.blit(image, rect)
                self.resp.append(img[i][2])
                x += 280
        except Exception, ex:
            print ex

    def load_font(self):
        x =140
        try:
            self.array_rect = []
            for i in range(4):
                image = self.image_load(font[i][0])
                rect = image.get_rect()
                rect.left = x
                rect.top = 580
                self.array_rect.append(rect)
                self.ventana.blit(image, rect)
                x += 280
            pygame.display.flip()

        except Exception, ex:
            print ex

    def validate(self):
        exito = False
        try:
            if len(self.resp_font) == 4:
                for x in range(4):
                    if self.resp[x] == self.resp_font[x]:
                        exito = True
                    else:
                        exito = False
                        break

                if exito:
                    self.print_font("Buen Trabajo",420,70)
                    self.principal()

                else:
                    self.print_font("Intente nuevamente",400,70)
                    del self.resp_font[:]

            else:
                pass
        except Exception, ex:
            print ex

    def val_orden(self, posl):
        ver = False
        for x in range(4):
            self.dic[x]=self.mt[x]
        self.dic_letter[posl] = self.pos_letter
        if(len(self.dic_letter)==4):
            for x in range(4):
                if (self.dic[x] == self.dic_letter[x]):
                    ver = True
                else:
                    ver = False
                    break
            if ver:
                self.print_font("Buen Trabajo",420,70)
                self.principal()
            else:
                self.pos_letter = -1
                self.print_font("Intente nuevamente",400,70)
                self.dic_letter.clear()

    def print_font(self, text, x, y):
        try:
            texto = pygame.font.SysFont(self.font_type, self.font_size)
            texto_present = texto.render(text,
            True, (0,0,0), (self.color))
            self.ventana.blit(texto_present,(x,y))
            pygame.display.update()
            pygame.time.wait(2000)
            texto_present = texto.render(text,
            True, (self.color), (self.color))
            self.ventana.blit(texto_present,(x,y))
            pygame.display.update()

        except Exception, ex:
            print ex

    def rosca(self, letter):
        self.resp_font.append(letter)
        self.validate()

    def detection_click(self):
        while True:
            while gtk.events_pending():
            	gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if self.array_rect[0].collidepoint(pos):
                        self.val_orden(0)
                        self.pos_letter += 1


                    if self.array_rect[1].collidepoint(pos):
                        self.val_orden(1)
                        self.pos_letter += 1


                    if self.array_rect[2].collidepoint(pos):
                        self.val_orden(2)
                        self.pos_letter += 1


                    if self.array_rect[3].collidepoint(pos):
                        self.val_orden(3)
                        self.pos_letter += 1


if __name__=='__main__':
    Main_Class()
