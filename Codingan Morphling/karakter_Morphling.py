import pygame
from abc import ABC, abstractmethod
from gambar_Morphling import *


class Karakter (ABC):
    playerx = 75
    playery = 500

    @abstractmethod
    def draw (self,screen):
        screen.blit(self.__image, self.rect)
    
    @abstractmethod
    def bergerak (self):
        if self.__lari == True:
            self.__image = self.__image_lari[self.__index % 8]
            self.__index += 1

    @abstractmethod
    def update (self,user_input):
        if self.__index > 5:
            self.__index = 0
        #gravity
        if self.__lari is True:
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
    
class Dino (Karakter):
    def __init__(self):
        self.__player_vel = 11
        self.__player_y = 490

        self.__image       = Gambar_Dino_Awal
        self.__dino_lari   = Gambar_Dino_Lari
        self.__dino_lompat = Gambar_Dino_Melompat
        self.__dino_nunduk = Gambar_Dino_Nunduk

        self.gojo_rect   = self.__image.get_rect()
        self.gojo_rect.x = self.playerx
        self.gojo_rect.y = self.playery
        self.gojo_vel    = self.__player_vel

        self.__index  = 0
        self.__lompat = False 
        self.__nunduk = False
        self.__lari   = True
    
        if self.__index == 12:
            self.__index =0

    def melompat (self):
        if self.__lompat is True:
            self.__image = self.__dino_lompat[self.__index % 12]
            self.gojo_rect.y -= self.gojo_vel * 5
            self.gojo_vel -= 1
            if self.gojo_vel < -self.__player_vel:
                self.__lompat = False
                self.gojo_vel = self.__player_vel
                self.gojo_rect.y = self.__player_y
            self.__index += 1
            

    def menunduk (self):
        if self.__nunduk is True:
            self.__image       = self.__dino_nunduk[self.__index % 4]
            self.gojo_rect.y = self.__player_y + 40
            self.__index      += 1
    
    def bergerak(self):
        if self.__lari is True:
            self.gojo_rect.y = self.__player_y
            self.__image = self.__dino_lari[self.__index % 8]
            self.__index += 1
    
    def melompat_evo (self):
        if self.__lompat is True:
            self.__image = self.__dino_lompat_evo[self.__index % 12]
            self.gojo_rect.y -= self.gojo_vel * 5
            self.gojo_vel -= 1
            if self.gojo_vel < -self.__player_vel:
                self.__lompat = False
                self.gojo_vel = self.__player_vel
                self.gojo_rect.y = self.__player_y
            self.__index += 1

    def menunduk_evo (self):
        if self.__nunduk is True:
            self.__image       = self.__dino_nunduk_evo[self.__index % 4]
            self.gojo_rect.y = self.__player_y - 10
            self.__index      += 1

    def bergerak_evo(self):
        if self.__lari is True:
            self.gojo_rect.y = self.__player_y
            self.__image = self.__dino_lari_evo[self.__index % 8]
            self.__index += 1

    def update (self, user_input,evo):
        if evo == False:
            self.__player_vel = 11
            self.gojo_recty = 490
            self.__player_y = self.gojo_recty

            if self.__index >= 12:
                self.__index =0
    
            if self.__lompat   is True:
                self.melompat()
            elif self.__nunduk is True:
                self.menunduk()
            elif self.__lari   is True:
                self.bergerak()
        
            if (self.__lompat is False and user_input[pygame.K_UP] ) or (self.__lompat is False and user_input[pygame.K_SPACE]) :
                jump_sound = pygame.mixer.Sound('Music/Jump.ogg') 
                jump_sound.play()
                self.__lompat = True
                self.__nunduk = False
                self.__lari = False
            elif (self.__nunduk is False and user_input[pygame.K_DOWN]):
                self.__lompat = False
                self.__nunduk = True
                self.__lari = False
            elif not (self.__lompat or user_input[pygame.K_DOWN]):
                self.__nunduk = False
                self.__lari = True
                self.__lompat = False
        elif evo == True:
            self.__player_vel = 11
            self.__player_y = 360
            self.__dino_lari_evo   = Gambar_Dino_Lari_evo
            self.__dino_lompat_evo = Gambar_Dino_Melompat_evo
            self.__dino_nunduk_evo = Gambar_Dino_Nunduk_evo

            if self.__index >= 12:
                self.__index =0
    
            if self.__lompat   is True:
                self.melompat_evo()
            elif self.__nunduk is True:
                self.menunduk_evo()
            elif self.__lari   is True:
                self.bergerak_evo()
        
            if (self.__lompat is False and user_input[pygame.K_UP] ) or (self.__lompat is False and user_input[pygame.K_SPACE]) :
                self.__lompat = True
                self.__nunduk = False
                self.__lari = False
            elif (self.__nunduk is False and user_input[pygame.K_DOWN]):
                self.__lompat = False
                self.__nunduk = True
                self.__lari = False
            elif not (self.__lompat or user_input[pygame.K_DOWN]):
                self.__nunduk = False
                self.__lari = True
                self.__lompat = False

    def draw (self,screen):
        screen.blit(self.__image, self.gojo_rect)

class Ptero(Karakter):
    def __init__(self):
        self.__x = 100
        self.__y = 936 // 2
        self.__image = Gambar_Ptero[0]
        self.rect = self.__image.get_rect()
        self.ptero_rect = self.rect
        self.ptero_rect.center = [self.__x,self.__y]
        #tambahin animasi wing flapping 
        self.vel = 0
        self.__terbangg = False  
        self.__flap = True
        self.__ptero_flapping = Gambar_Ptero
        self.__index = 0

    def terbang (self):
        if self.__terbangg == True:
            self.vel = -15
            self.__terbangg = False

    def bergerak (self):
        if self.__flap == True:
            self.__image = self.__ptero_flapping[self.__index % 8]
            self.__index += 1

    def update (self,user_input):
        if self.__index > 5:
            self.__index = 0
        #gravity
        if self.__flap is True:
            self.bergerak()
            self.vel += 4
        if self.vel > 12:
            self.vel = 12
        if self.rect.bottom < 936:
            self.rect.y += self.vel
        if self.rect.top < 0:
            self.rect.top = 0 
        #jump
        if self.__terbangg is False and user_input[pygame.K_SPACE]:
            self.__terbangg = True
            self.terbang()
    
    def draw(self,screen):
        screen.blit(self.__image,self.rect)		
