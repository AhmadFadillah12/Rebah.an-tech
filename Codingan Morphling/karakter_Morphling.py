import pygame
from abc import abstractmethod
from gambar_Morphling import *


class Karakter ():
    playerx = 75
    playery = 500

    @abstractmethod
    def bergerak (self):
       pass

    def berhenti (self):
       pass
    
    def evolusi (self):
       pass

    @abstractmethod
    def update(self):
        pass

class Dino (Karakter):
    def __init__(self):
        self.player_vel = 11
        self.player_y = 490# batas sementara

        self.image       = Gambar_Dino_Awal
        self.dino_lari   = Gambar_Dino_Lari
        self.dino_lompat = Gambar_Dino_Melompat
        self.dino_nunduk = Gambar_Dino_Nunduk

        self.gojo_rect   = self.image.get_rect()
        self.gojo_rect.x = self.playerx
        self.gojo_rect.y = self.playery
        self.gojo_vel    = self.player_vel

        self.index  = 0
        self.lompat = False 
        self.nunduk = False
        self.lari   = True

    def melompat (self):
        if self.lompat is True:
            # pygame.mixer.music.load('Gambarrr/sound_lompat.mp3') 
            # pygame.mixer.music.play()
            self.image = self.dino_lompat[self.index % 12]
            self.gojo_rect.y -= self.gojo_vel * 5
            self.gojo_vel -= 1
            if self.gojo_vel < -self.player_vel:
                self.lompat = False
                self.gojo_vel = self.player_vel
                self.gojo_rect.y = self.player_y
            self.index += 1

    def menunduk (self):
        if self.nunduk is True:
            self.image       = self.dino_nunduk[self.index % 4]
            self.gojo_rect.y = self.player_y + 40
            self.index      += 1

    def bergerak(self):
        if self.lari is True:
            self.gojo_rect.y = self.player_y
            self.image = self.dino_lari[self.index % 8]
            self.index += 1

    def update (self, user_input):
        if self.index >= 12:
            self.index =0
 
        if self.lompat   is True:
            self.melompat()
        elif self.nunduk is True:
            self.menunduk()
        elif self.lari   is True:
            self.bergerak()
    
        if (self.lompat is False and user_input[pygame.K_UP] ) or (self.lompat is False and user_input[pygame.K_SPACE]) :
            self.lompat = True
            self.nunduk = False
            self.lari = False
        elif (self.nunduk is False and user_input[pygame.K_DOWN]):
            self.lompat = False
            self.nunduk = True
            self.lari = False
        elif not (self.lompat or user_input[pygame.K_DOWN]):
            self.nunduk = False
            self.lari = True
            self.lompat = False

    def draw (self,screen):
        screen.blit(self.image, (self.gojo_rect.x, self.gojo_rect.y))

class BurungTerbang(Karakter):
    def __init__(self):
        self.x = 100
        self.y = 936 // 2
        self.image = Gambar_Ptero[0]
        self.rect = self.image.get_rect()
        self.ptero_rect = self.rect
        self.ptero_rect.center = [self.x,self.y]
        #tambahin animasi wing flapping 
        self.vel = 0
        self.terbangg = False  
        self.flap = True
        self.ptero_flapping = Gambar_Ptero
        self.index = 0

    def terbang (self):
        if self.terbangg == True:
            self.vel = -15
            self.terbangg = False

    def bergerak (self):
        if self.flap == True:
            self.image = self.ptero_flapping[self.index % 8]
            self.index += 1

    def update (self,user_input):
        if self.index > 5:
            self.index = 0
        #gravity
        if self.flap is True:
            self.bergerak()
            self.vel += 4
        if self.vel > 12:
            self.vel = 12
        if self.rect.bottom < 936:
            self.rect.y += self.vel
        if self.rect.top < 0:
            self.rect.top = 0 
        #jump
        if self.terbangg is False and user_input[pygame.K_SPACE]:
            self.terbangg = True
            self.terbang()
    
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))		
