from abc import abstractmethod
from subprocess import DETACHED_PROCESS
import pygame
import random

pygame.init()
#Membuat screen, title, dan icon
width = 1100
height = 836
screen = pygame.display.set_mode((width,height))
font = pygame.font.Font('freesansbold.ttf',20)
pygame.display.set_caption ("Morphling")
icon = pygame.image.load ('Codingan Morphling/Gambarrr/pterodactyl.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Codingan Morphling/Gambarrr/background.png')
background = pygame.transform.scale(background,(width,height))
background_menu = pygame.image.load('Codingan Morphling/Gambarrr/menu_start.png')
background_menu = pygame.transform.scale(background_menu,(950,836)) 
pipa = pygame.image.load('Codingan Morphling/Gambarrr/Pipa/pipa 1.png')
pipa = pygame.transform.flip(pipa, False, True)
pipaatas = pygame.image.load('Codingan Morphling/Gambarrr/Pipa/pipa 2.png')
pipa = pygame.transform.scale(pipa, (80, 380))
pipaatas = pygame.transform.scale(pipaatas, (110, 380))
background_ptero = pygame.image.load('Codingan Morphling/Gambarrr/FinalNight1.png')
background_ptero = pygame.transform.scale(background_ptero,(875,936))


#sementara code gambar di satukan sama code gamenya sebelum dipisah setelah fix gambarnya
Gambar_Dino_Awal   =    pygame.image.load('Codingan Morphling/Gambarrr/dino_idle.png')
Gambar_Dino_Nunduk =   [pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Mati/Dead (2).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Mati/Dead (3).png')] # sementara


Gambar_Dino_Lari   =   [pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lari/Run (1).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lari/Run (2).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lari/Run (3).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lari/Run (4).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lari/Run (5).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lari/Run (6).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lari/Run (7).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lari/Run (8).png')]

Gambar_Dino_Melompat = [pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (1).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (2).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (3).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (4).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (5).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (6).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (7).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (8).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (9).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (10).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (11).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Lompat/Jump (12).png')]

Gambar_Obstacle_Batu = [pygame.image.load('Codingan Morphling/Gambarrr/Batu/Crystal2.png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Batu/Crystal4.png')]

Gambar_Ptero = [pygame.image.load('Codingan Morphling/Gambarrr/Ptero/pterodactyl.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/pterodactyl2.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/pterodactyl3.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/pterodactyl4.png')]


Gambar_Obstacle_Batu[0] = pygame.transform.scale(Gambar_Obstacle_Batu[0],(90,90))
Gambar_Obstacle_Batu[1] = pygame.transform.scale(Gambar_Obstacle_Batu[1],(90,90))
pohon = pygame.image.load('Codingan Morphling/Gambarrr/Pohon/7.png')
pohon = pygame.transform.scale(pohon, (90, 130))
bird = pygame.image.load('Codingan Morphling/Gambarrr/seagull.png')
pohonbesar = pygame.image.load('Codingan Morphling/Gambarrr/Pohon/1.png')
pohonbesar = pygame.transform.scale(pohonbesar, (130, 120))

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
            # pygame.mixer.music.load('Codingan Morphling/Gambarrr/sound_lompat.mp3') 
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
    def __init__(self):
        self.x = 100
        self.y = 936 // 2
        self.image = pygame.image.load('Codingan Morphling/Gambarrr/Ptero/pterodactyl.png')
        self.image = pygame.transform.scale(self.image, (85, 85))
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
            self.image = self.ptero_flapping[self.index % 4]
            self.index += 1

    def update (self,user_input):
        if self.index > 5:
            self.index = 0
        global TERBANG
        #gravity
        if self.flap is True:
            self.bergerak()

        if TERBANG == True:
            self.vel += 3
            if self.vel > 10:
                self.vel = 10
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
                obstacles.append(Pohon(pohon))

    def buat_rintangan (self):
        for rintangan in obstacles:
            rintangan.draw(screen)
            rintangan.update()
            if player1.gojo_rect.colliderect(rintangan.rect):
                death += 1
                start(Score.hitung_score(self))
                

class Pohon(Obstacle):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 500

class PohonBesar(Obstacle):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 530
    
class Batu(Obstacle):
    def __init__(self, image,type):
        self.type = type
        self.image = image[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 540

class Bird(Obstacle):
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(450,500)

class Obstacle_pipa ():
    def update(self):
        self.rect.x -= speed
       
    def ganti_rintangan(self):
            x = random.randint(300 , 700)
            pipaa = pygame.transform.scale(pipa, (80, 936 - x - 170))
            pipaatass = pygame.transform.scale(pipaatas, (110, x))
            if poin % 50 == 0 and poin < 1000:
                obstacles.append(Pipa(pipaa,1))
                obstacles.append(Pipa(pipaatass,-1))
            if poin > 1000 and poin < 2000: 
                if poin % 40== 0:
                    obstacles.append(Pipa(pipaa,1))
                    obstacles.append(Pipa(pipaatass,-1))
            if poin > 2000 and poin < 3000:
                if poin % 30 == 0:
                    obstacles.append(Pipa(pipaa,1))
                    obstacles.append(Pipa(pipaatass,-1))
    
    def buat_rintangan(self):
        for rintangan in obstacles:
            rintangan.draw(screen)
            rintangan.update()
            if player.ptero_rect.colliderect(rintangan.rect):
                death += 1
                start(Score.hitung_score(self))
                

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Pipa(Obstacle_pipa):
    def __init__(self,image,posisi):
        self.image = image
        self.rect = self.image.get_rect()
        if posisi == 1: 
            self.rect.bottomleft = (885,950)
        if posisi == -1:
            self.rect.topleft = (850,0)

class Score:
    def hitung_score(self):
        global poin, speed
        poin+=1
        if poin % 150 == 0:
            speed += 0.5

        text = font.render("Score: " + str(poin), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (800, 100)
        screen.blit(text, textRect)
        return poin

    def high_score():
        high_score = 0
        high_score_file = open("Codingan Morphling/high_score.txt", "r")
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

button_start = pygame.image.load('Codingan Morphling/Gambarrr/button_start.png')
start_button = Button(480,500,button_start,0.9)
button_end = pygame.image.load('Codingan Morphling/Gambarrr/exitt.png')
end_button = Button(480,620,button_end,0.9)
game_dino = pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino idle/idle (1).png')
game_dino = pygame.transform.scale(game_dino,(150,150))
dino_game = Button(715,395,game_dino,1.15)
game_ptero = pygame.image.load('Codingan Morphling/Gambarrr/Ptero/pterodactyl.png')
ptero_game = Button(200,400,game_ptero,0.9)

gameover =  pygame.image.load('Codingan Morphling/Gambarrr/Background/gameover_dino.png')
gameover = pygame.transform.scale(gameover,(950,836))
def start (nilai):
    running = True
    while running: 
        pygame.display.set_mode((950,836))
        screen.fill((255,255,255))
        screen.blit(background_menu,(0,0))
        if start_button.draw():
            pilih_karakter()
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

background_select = pygame.image.load('Codingan Morphling/Gambarrr/Background/character_select.jpeg')
background_select = pygame.transform.scale(background_select,(950,836))

def pilih_karakter():
    running = True
    while running: 
        screen.fill((225,225,255))
        screen.blit(background_select,(0,0))

        if dino_game.draw():
            game_dino()
        if ptero_game.draw():
            game_ptero()
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

def game_dino ():
    pygame.display.set_mode((width,height))
    global poin, speed ,obstacles,player1
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
                pygame.quit()
                exit()

        clock.tick(25)
        score.hitung_score()
        pygame.display.update()

 
TERBANG = False
game_over = False

def game_ptero ():
    global TERBANG, poin ,speed,game_over,pipa,obstacles,player,pipaatas,counter
    game_over = False
    running = True
    speed = 8
    poin = 0
    score = Score()
    clock = pygame.time.Clock()
    obstacles = []
    i = 0
    width = 870
    height = 936
    player = BurungTerbang()
    obstacle = Obstacle_pipa()
    pygame.display.set_mode((width,height))

    while running: 
        if game_over == False: 
            screen.fill((255,255,255))
            screen.blit(background_ptero, (i,0))
            screen.blit(background_ptero, (width+i,0))
            if i <= -width:
                screen.blit(background_ptero, (width+i,0))
                i = 0
            i -= speed

            player.draw(screen)
            obstacle.ganti_rintangan()
            obstacle.buat_rintangan()
            user_input = pygame.key.get_pressed()
            player.update(user_input)
            
            if player.rect.bottom > 936:
                game_over = True
                TERBANG = False

            score.hitung_score()
            clock.tick(30)
            pygame.display.update()
            
        else: 
            start(0)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and TERBANG == False and game_over == False:
                TERBANG = True

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

        
start(0)