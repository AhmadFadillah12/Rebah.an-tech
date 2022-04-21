from abc import abstractmethod
import pygame
import random

pygame.init()

#Membuat screen, title, dan icon
width = 950
height = 836
screen = pygame.display.set_mode((width,height))
font = pygame.font.Font('freesansbold.ttf',20)
pygame.display.set_caption ("Morphling")
icon = pygame.image.load ('Gambarrr/pterodactyl.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Gambarrr/background.png')

class Karakter ():
    playerx = 75
    playery = 570

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

Gojo = pygame.image.load('Gambarrr/150px dino.png')

class BurungDarat (Karakter):
    playerx = 75
    playery = 570
    player_vel = 8

    def __init__(self):
        self.gojox = self.playerx
        self.gojoy = self.playery
        self.gojo_vel = self.player_vel
        self.lompat = False
        self.nunduk = False

    def draw (self,screen):
        screen.blit(Gojo, (self.gojox, self.gojoy))

    def melompat (self,user_input):
        if (self.lompat is False and user_input[pygame.K_UP] ) or (self.lompat is False and user_input[pygame.K_SPACE]) :
            self.lompat = True

        if self.lompat is True:
            self.gojoy -= self.gojo_vel
            self.gojo_vel -= 0.1
            if self.gojo_vel < -self.player_vel:
                self.lompat = False
                self.gojo_vel = self.player_vel

    def menunduk (self,user_input):
        if (self.nunduk is False and user_input[pygame.K_DOWN] ) :
            self.nunduk = True
        

    def bergerak(self):
        pass
    def update (self, user_input):
        pass

class BurungTerbang(Karakter):
	def terbang (self):
		pass
	def update (self):
		pass
	def bergerak (self):
		pass
	def draw(self):
		pass
		
class Obstacle:
    def buat_rintangan(self, screen):
        pass
        
    def ganti_rintangan():
        pass
    def update():
        pass

class Pohon(Obstacle):
    def update():
        pass
    
class Batu(Obstacle):
    def update():
        pass

class LoveBird(Obstacle):
    def update():
        pass

class Pipa(Obstacle):
    def update():
        pass

class Score:
    def hitung_score():
        score = 0
        game_speed = 20
        score+=1
        if score % 100 == 0:
            game_speed +=1

        text = font.render("Score: " + str(score), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (800, 100)
        screen.blit(text, textRect)
        
    def recent_score():
        pass
    def high_score():
        pass
    
    
player1 = BurungDarat()
running = True 
i = 0
obstacles = []
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(background, (i,0))
    screen.blit(background, (width+i,0))
    if i == -width:
        screen.blit(background, (width+i,0))
        i = 0
    i -= 0.1

    player1.draw(screen)
    user_input = pygame.key.get_pressed()
    player1.melompat(user_input)
    
    Score.hitung_score()
    pygame.display.update()