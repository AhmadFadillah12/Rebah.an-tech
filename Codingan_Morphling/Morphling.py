from abc import abstractmethod
import pygame
import random
import os

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

gojo = pygame.image.load('Gambarrr/150px dino.png')
gojo_nunduk = pygame.image.load('Gambarrr/pterodactyl.png')
poh = pygame.image.load(os.path.join('Gambarrr/tree.jpg'))
poh = pygame.transform.scale(poh, (69, 69))
class BurungDarat (Karakter):
    playerx = 75
    playery = 570
    player_vel = 8

    def __init__(self):
        self.image = gojo
        self.rect = self.image.get_rect()
        self.rect.x = self.playerx
        self.rect.y = self.playery
        self.gojo_vel = self.player_vel
        self.lompat = False
        self.nunduk = False
        self.lari = True

    def melompat (self):
        self.image = gojo
        if self.lompat is True:
            self.rect.y -= self.gojo_vel * 4
            self.gojo_vel -= 0.8
            if self.gojo_vel < -self.player_vel:
                self.lompat = False
                self.gojo_vel = self.player_vel

    def menunduk (self):
        
        if self.nunduk is True:
            self.image = gojo_nunduk


    def bergerak(self):
        pass
    def update (self, user_input):
        if self.lompat:
            self.melompat()
        elif self.nunduk:
            self.menunduk()
            

        if (self.lompat is False and user_input[pygame.K_UP] ) or (self.lompat is False and user_input[pygame.K_SPACE]) :
            self.lompat = True
            self.nunduk = False
        elif (self.nunduk is False and user_input[pygame.K_DOWN]):
            self.lompat = False
            self.nunduk = True
        pass

    def draw (self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


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
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x <-self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Pohon(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 620
    
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
    


global points, game_speed,obstacles
player1 = BurungDarat()
running = True 
i = 0
obstacles = []
points = 0
game_speed = 14
clock = pygame.time.Clock()
FPS = 25

def scores():
    global points, game_speed
    points+=1

    text = font.render("Score: " + str(points), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (800, 100)
    screen.blit(text, textRect)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(background, (i,0))
    screen.blit(background, (width+i,0))
    if i <= -width:
        screen.blit(background, (width+i,0))
        i = 0
    i -= 4

    player1.draw(screen)
    user_input = pygame.key.get_pressed()
    player1.update(user_input)

    if len(obstacles) == 0:
        obstacles.append(Pohon(poh))

    for obstacle in obstacles:
        obstacle.draw(screen)
        obstacle.update()
        if player1.rect.colliderect(obstacle.rect):
            pygame.time.delay(2000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    scores()
    pygame.display.update()