import pygame

pygame.init()

#Membuat screen, title, dan icon
width = 950
height = 836
screen = pygame.display.set_mode((950,836))
pygame.display.set_caption ("Morphling")
icon = pygame.image.load ('Gambarrr/pterodactyl.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Gambarrr/background.png')

class Karakter ():
    playerx = 75
    playery = 570

    def bergerak (self):
       pass

    def berhenti (self):
       pass
    
    def Evolusi (self):
       pass

    def Update(self):
        pass

Gojo = pygame.image.load('Gambarrr/150px dino.png') 

class Burung_darat (Karakter):
    playerx = 75
    playery = 570
    player_vel = 8

    def __init__(self):
        self.gojox = self.playerx
        self.gojoy = self.playery
        self.gojo_vel = self.player_vel
        self.lompat = False

    def draw (self,screen):
        screen.blit(Gojo, (self.gojox, self.gojoy))

    def melompat (self,UserInput):
        if (self.lompat is False and UserInput[pygame.K_UP] ) or (self.lompat is False and UserInput[pygame.K_SPACE]) :
            self.lompat = True

        if self.lompat is True:
            self.gojoy -= self.gojo_vel 
            self.gojo_vel -= 0.1
            if self.gojo_vel < -self.player_vel:
                self.lompat = False
                self.gojo_vel = self.player_vel
    def menunduk (self):
        pass
    def bergerak(self):
        pass
    def update (self, UserInput):
        pass

class Burung_Terbang(Karakter):
	def Terbang (self):
		pass
	def Update (self):
		pass
	def Bergerak (self):
		pass
	def draw(self):
		pass
		
class Obstacle:
    def Buat_Rintangan():
        pass
    def Ganti_Rintangan():
        pass
    def Update():
        pass

class Pohon(Obstacle):
    def Update():
        pass
    
class Batu(Obstacle):
    def Update():
        pass

class Love_bird(Obstacle):
    def Update():
        pass

class Pipa(Obstacle):
    def Update():
        pass

class Score:
    def Hitung_score():
        pass
    def Recent_score():
        pass
    def High_score():
        pass
    
    
player1 = Burung_darat()
running = True 
i = 0
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
    UserInput = pygame.key.get_pressed()
    player1.melompat(UserInput)
    
    pygame.display.update()