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
background = pygame.image.load('Gambarrr/bg.jpeg')
gojo = pygame.image.load('Gambarrr/150px dino.png')
gojo_nunduk = pygame.image.load('Gambarrr/pterodactyl.png')
pohon = pygame.image.load('Gambarrr/christmas-tree.png')
pohon = pygame.transform.scale(pohon, (85, 85))
rock = pygame.image.load('Gambarrr/rock.png')
rock = pygame.transform.scale(rock, (70, 70))
bird = pygame.image.load('Gambarrr/seagull.png')
pohonbesar = pygame.image.load('Gambarrr/forest.png')
pohonbesar = pygame.transform.scale(pohonbesar, (115, 115))
crystal = [pygame.image.load('Gambarrr/crystal1.png'), pygame.image.load('Gambarrr/crystal2.png')]

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

class BurungDarat (Karakter):
    def __init__(self):
        self.player_vel = 11
        self.image = gojo
        self.gojo_rect = self.image.get_rect()
        self.gojo_rect.x = self.playerx
        self.gojo_rect.y = self.playery
        self.gojo_vel = self.player_vel
        self.lompat = False 
        self.nunduk = False
        self.lari = True

    def melompat (self):
        if self.lompat is True:
            pygame.mixer.music.load('SOUND_FLAPPY/audio/hit.wav')
            pygame.mixer.music.play()
            self.gojo_rect.y -= self.gojo_vel * 4
            self.gojo_vel -= 1
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
        screen.blit(self.image, (self.gojo_rect.x, self.gojo_rect.y))


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
    
    def update(self):
        self.rect.x -= speed
        if self.rect.x <-self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def ganti_rintangan (self):
        if obstacles == []:
            x = random.randint(0,3)
            if x == 0:
                obstacles.append(Pohon(pohon))
            elif x == 1:
                x = random.randint(0,1)
                obstacles.append(Batu(crystal,x))
            elif x == 2:
                obstacles.append(Bird(bird))
            elif x == 3:
                obstacles.append(PohonBesar(pohonbesar))

    def buat_rintangan (self):
        for rintangan in obstacles:
            rintangan.draw(screen)
            rintangan.update()
            if player1.gojo_rect.colliderect(rintangan.rect):
                start()

class Pohon(Obstacle):
    def __init__(self, image):
        self.image = image
        x = random.randint(70,100)
        self.image = pygame.transform.scale(self.image, (x, x))
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 600

class PohonBesar(Obstacle):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 600
    
class Batu(Obstacle):
    def __init__(self, image,type):
        self.type = type
        self.image = image[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 625

class Bird(Obstacle):
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(500,625)

class Pipa(Obstacle):
    def update():
        pass

class Score:
    def hitung_score(self):
        global poin, speed
        poin+=1
        if poin % 150 == 0:
            speed +=1

        text = font.render("Score: " + str(poin), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (800, 100)
        screen.blit(text, textRect)

    def recent_score():
        pass
    def high_score():
        pass

def start ():
    running = True
    while running: 
        screen.fill((255,255,255))
        font = pygame.font.SysFont("verdana", 20)
        text = font.render("Press Space or Arrow Up Key to Start",True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (width//2, height//2)
        screen.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:    
                game()
        
def game ():
    global poin, speed,obstacles,death,player1
    player1 = BurungDarat()
    running = True 
    i = 0
    obstacles = []
    poin = 0
    speed = 15
    clock = pygame.time.Clock()
    score = Score()
    obstacle = Obstacle()

    while running: 
        
        screen.fill((255,255,255))
        screen.blit(background, (i,0))
        screen.blit(background, (width+i,0))
        if i <= -width:
            screen.blit(background, (width+i,0))
            i = 0
        i -= speed

        #Menampilkan user dan mengatur gerakannya
        player1.draw(screen)
        user_input = pygame.key.get_pressed()
        player1.update(user_input)

        #Membuat rintangan 
        obstacle.ganti_rintangan()
        obstacle.buat_rintangan()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(30)
        score.hitung_score()
        pygame.display.update()

start()