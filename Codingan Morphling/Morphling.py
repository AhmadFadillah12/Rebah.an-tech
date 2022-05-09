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
background = pygame.transform.scale(background,(950,836))
background_menu = pygame.image.load('Gambarrr/menu_start.png')
background_menu = pygame.transform.scale(background_menu,(950,836))

Gambar_Obstacle_Batu[0] = pygame.transform.scale(Gambar_Obstacle_Batu[0],(100,100))
Gambar_Obstacle_Batu[1] = pygame.transform.scale(Gambar_Obstacle_Batu[1],(100,100))
pohon = pygame.image.load('Gambarrr/Pohon/7.png')
pohon = pygame.transform.scale(pohon, (100, 150))
bird = pygame.image.load('Gambarrr/seagull.png')
pohonbesar = pygame.image.load('Gambarrr/Pohon/1.png')
pohonbesar = pygame.transform.scale(pohonbesar, (130, 130))

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
        self.player_nunduk = 600 # batas sementara

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
            self.index += 1
    def menunduk (self):
        if self.nunduk is True:
            self.image       = self.dino_nunduk[self.index % 2]
            self.gojo_rect.y = self.player_nunduk
            self.index      += 1

    def bergerak(self):
        if self.lari is True:
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
        elif (self.nunduk is False and user_input[pygame.K_DOWN]):
            self.lompat = False
            self.nunduk = True
        

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
                obstacles.append(Batu(Gambar_Obstacle_Batu,x))
            elif x == 2:
                obstacles.append(Bird(bird))
            elif x == 3:
                obstacles.append(PohonBesar(pohonbesar))

    def buat_rintangan (self):
        for rintangan in obstacles:
            rintangan.draw(screen)
            rintangan.update()
            if player1.gojo_rect.colliderect(rintangan.rect):
                start(Score.hitung_score(self))

class Pohon(Obstacle):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 480

class PohonBesar(Obstacle):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 520
    
class Batu(Obstacle):
    def __init__(self, image,type):
        self.type = type
        self.image = image[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 530

class Bird(Obstacle):
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(480,500)

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
        return poin

    def high_score():
        high_score = 0
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        return high_score

    def save_high_score(new_high_score):
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()


class Button: 
    def __init__(self, x , y ,image , scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (int(self.width * scale) , int(self.height * scale)))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image,(self.rect.x , self.rect.y))
        return action

button_start = pygame.image.load('Gambarrr/button_start.png')
start_button = Button(480,500,button_start,0.9)
button_end = pygame.image.load('Gambarrr/exitt.png')
end_button = Button(480,620,button_end,0.9)
def start (nilai):
    running = True
    while running: 
        screen.fill((255,255,255))
        screen.blit(background_menu,(0,0))
        if start_button.draw():
            game()
        if end_button.draw():
            running = False
            pygame.quit()
            exit()
        score = font.render("Your Score: " + str(nilai), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (width // 2, height // 2 + 20)
        screen.blit(score, scoreRect)
        high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
        high_scoreRect = high_score.get_rect()
        high_scoreRect.center = (width // 2, height // 2 )
        screen.blit(high_score, high_scoreRect)
        if nilai >Score.high_score():
            Score.save_high_score(nilai)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
    
def game ():
    global poin, speed,obstacles,death,player1
    player1 = Dino()
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

start(0)
