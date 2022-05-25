import pygame
import random
from abc import ABC, abstractmethod

pygame.init()

#Ukuran Window
width = 1100
height = 836
screen = pygame.display.set_mode((width,height))
font = pygame.font.Font('freesansbold.ttf',20)
pygame.display.set_caption ("Morphling")
icon = pygame.image.load ('Gambarrr/pterodactyl.png')
pygame.display.set_icon(icon)

#Background Ptero
background_ptero = pygame.image.load('Gambarrr/FinalNight1.png')
background_ptero = pygame.transform.scale(background_ptero,(875,936))

#Background How to Play
background_how_to = pygame.image.load('Gambarrr/Background/howtoplay.jpg')
background_how_to = pygame.transform.scale(background_how_to,(950,836))

#Background Credits
background_credits = pygame.image.load('Gambarrr/Background/credits_bg.jpg')
background_credits = pygame.transform.scale(background_credits,(950,836))

#Gambar Karakter
Gambar_Dino_Awal         =    pygame.image.load('Gambarrr/dino_idle.png')
Gambar_Dino_Nunduk       = [pygame.image.load(f'Gambarrr/Dino/Dino Nunduk/Proses Nunduk{i+1}.png')         for i in range (0,4) ]
Gambar_Dino_Lari         = [pygame.image.load(f'Gambarrr/Dino/Dino Lari/Run ({i+1}).png')                  for i in range (0,8) ]
Gambar_Dino_Melompat     = [pygame.image.load(f"Gambarrr/Dino/Dino Lompat/Jump ({i+1}).png")               for i in range(0,12) ]

Gambar_Dino_Awal_evo     =    pygame.image.load('Gambarrr/dino_idle.png')
Gambar_Dino_Nunduk_evo   = [pygame.image.load(f'Gambarrr/Dino/Evolusi/Dino Nunduk/Proses Nunduk{i+1}.png') for i in range (0,4) ]
Gambar_Dino_Lari_evo     = [pygame.image.load(f'Gambarrr/Dino/Evolusi/Dino Lari/Run ({i+1}).png')          for i in range (0,8) ]
Gambar_Dino_Melompat_evo = [pygame.image.load(f'Gambarrr/Dino/Evolusi/Dino Lompat/Jump ({i+1}).png')       for i in range (0,12)]
Gambar_Obstacle_Batu     = [pygame.image.load(f'Gambarrr/Batu/Crystal{i+1}.png')                           for i in range (0,13)]
Gambar_Ptero             = [pygame.image.load(f'Gambarrr/Ptero/Pterodactyl{i+1}.png')                      for i in range (0,8) ]


#Gambar Obstacle Ptero
pipa = pygame.image.load('Gambarrr/Pipa/pipa 1.png')
pipa = pygame.transform.flip(pipa, False, True)
pipaatas = pygame.image.load('Gambarrr/Pipa/pipa 2.png')
pipa = pygame.transform.scale(pipa, (80, 380))
pipaatas = pygame.transform.scale(pipaatas, (110, 380))

#Gambar Obstacle Dino
Gambar_Obstacle_Batu[0] = pygame.transform.scale(Gambar_Obstacle_Batu[0],(90,90))
Gambar_Obstacle_Batu[1] = pygame.transform.scale(Gambar_Obstacle_Batu[1],(90,90))
pohon = pygame.image.load('Gambarrr/Pohon/7.png')
pohon = pygame.transform.scale(pohon, (90, 130))
bird = pygame.image.load('Gambarrr/seagull.png')
bird = pygame.transform.scale(bird, (70, 70))
pohonbesar = pygame.image.load('Gambarrr/Pohon/1.png')
pohonbesar = pygame.transform.scale(pohonbesar, (110, 120))
powerup = pygame.image.load('Gambarrr/Powerup/powerup.png')
powerup = pygame.transform.scale(powerup, (70, 70))

#Background memilih karakter   
background_select = pygame.image.load('Gambarrr/Background/character_select.jpeg')
background_select = pygame.transform.scale(background_select,(950,836))

#Background Menu Game
background_menu = pygame.image.load('Gambarrr/menu_start.png')
background_menu = pygame.transform.scale(background_menu,(950,836)) 

#Background Dino
background = pygame.image.load('Gambarrr/background.png')
background = pygame.transform.scale(background,(width,height))


class Karakter (ABC):
    playerx = 75
    playery = 500

    @abstractmethod
    def bergerak (self):
       if self.lari is True:
            self.gojo_rect.y = self.player_y
            self.image = self.dino_lari[self.index % 8]
            self.index += 1

    @abstractmethod
    def update(self,user_input):
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

    @abstractmethod
    def draw (self):
        screen.blit(self.image,self.rect)	

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
    
        if self.index == 12:
            self.index =0

    def melompat (self):
        if self.lompat is True:
            #pygame.mixer.music.load('Gambarrr/Music/Jump.ogg') 
            #pygame.mixer.music.play()
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
    
    def melompat_evo (self):
        if self.lompat is True:
            # pygame.mixer.music.load('Gambarrr/sound_lompat.mp3') 
            # pygame.mixer.music.play()
            self.image = self.dino_lompat_evo[self.index % 12]
            self.gojo_rect.y -= self.gojo_vel * 5
            self.gojo_vel -= 1
            if self.gojo_vel < -self.player_vel:
                self.lompat = False
                self.gojo_vel = self.player_vel
                self.gojo_rect.y = self.player_y
            self.index += 1

    def menunduk_evo (self):
        if self.nunduk is True:
            self.image       = self.dino_nunduk_evo[self.index % 4]
            self.gojo_rect.y = self.player_y - 10
            self.index      += 1

    def bergerak_evo(self):
        if self.lari is True:
            self.gojo_rect.y = self.player_y
            self.image = self.dino_lari_evo[self.index % 8]
            self.index += 1

    def update (self, user_input,evo):
        if evo == False:
            self.player_vel = 11
            self.gojo_recty = 490
            self.player_y = self.gojo_recty

            if self.index >= 12:
                self.index =0
    
            if self.lompat   is True:
                self.melompat()
            elif self.nunduk is True:
                self.menunduk()
            elif self.lari   is True:
                self.bergerak()
        
            if (self.lompat is False and user_input[pygame.K_UP] ) or (self.lompat is False and user_input[pygame.K_SPACE]) :
                jump_sound = pygame.mixer.Sound('Music/Jump.ogg') 
                jump_sound.play()
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
        elif evo == True:
            self.player_vel = 11
            self.player_y = 360
            self.dino_lari_evo   = Gambar_Dino_Lari_evo
            self.dino_lompat_evo = Gambar_Dino_Melompat_evo
            self.dino_nunduk_evo = Gambar_Dino_Nunduk_evo

            if self.index >= 12:
                self.index =0
    
            if self.lompat   is True:
                self.melompat_evo()
            elif self.nunduk is True:
                self.menunduk_evo()
            elif self.lari   is True:
                self.bergerak_evo()
        
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
        screen.blit(self.image, self.gojo_rect)

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
        screen.blit(self.image,self.rect)		

class Button: 
    def __init__(self, x , y ,image , scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.x = x
        self.y = y
        self.dino = True
        self.x_s = x
        self.y_s = y
        self.image = pygame.transform.scale(image, (int(self.width * scale) , int(self.height * scale)))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.clicked = False
        self.count=0

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.count<3:
                self.x+=1
                self.y+=1
                self.rect = self.image.get_rect(center=(self.x, self.y))
                self.count+=1
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.x = self.x_s
            self.y = self.y_s
            self.rect = self.image.get_rect(center=(self.x_s, self.y_s))
            self.count = 0

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image,(self.rect.x , self.rect.y))
        return action


#PILIHAN KARAKTER
#Tombol Start
button_start = pygame.image.load('Gambarrr/Background/button_start.png')
start_button = Button(480,450,button_start,0.8)

#Tombol How to play
how_to = pygame.image.load('Gambarrr/Background/howtoplay_button.png')
button_how_to = Button(480,530,how_to,0.15)

#Tombol Credits
credits = pygame.image.load('Gambarrr/Background/CREDITS.png')
button_credits = Button(480,610,credits,0.18)

#Tombol Exit
button_end = pygame.image.load('Gambarrr/Background/exitt.png')
end_button = Button(480,690,button_end,0.8)

#Gambar Dino di pilihan karakter
x=0
game_dino = Gambar_Dino_Lari [ x % 8]
game_dino = pygame.transform.scale(game_dino,(150,150))
dino_game = Button(715,395,game_dino,1.15)

#Gambar Ptero di pilihan karakter
game_ptero = pygame.image.load('Gambarrr/Ptero/pterodactyl5.png')
ptero_game = Button(200,400,game_ptero,1.5)


#PILIHAN KETIKA GAME OVER
#Tombol Play Again
gameover_button = pygame.image.load('Gambarrr/Background/PlayAgain.png')
button_gameover = Button(480,600,gameover_button,0.18)
gameover_button_ptero = pygame.image.load('Gambarrr/Background/PlayAgain_night.png')
button_gameover_ptero = Button(480,600,gameover_button_ptero,0.18)

#Tombol Exit
gameover_button_exit = pygame.image.load('Gambarrr/Background/button_exit.png')
button_gameover_exit = Button(480,680,gameover_button_exit,0.18)
gameover_button_exit_ptero = pygame.image.load('Gambarrr/Background/button_exit_night.png')
button_gameover_exit_ptero = Button(480,680,gameover_button_exit_ptero,0.18)

#Gambar Dino mati
gameover = pygame.image.load('Gambarrr/Background/gameover_dino.png')
gameover = pygame.transform.scale(gameover,(950,836))

#Gambar Ptero mati
gameover_ptero = pygame.image.load ('Gambarrr/Background/gameover_ptero.png')
gameover_ptero = pygame.transform.scale(gameover_ptero,(950,836))

class Obstacle:
    obstacles = []
    def update(self):
        if evo == True: 
            self.rect.x -= speed
            if self.rect.x > -self.rect.width:
                obstacles.pop()
        else:
            self.rect.x -= speed
            if self.rect.x <-self.rect.width:
                obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    @staticmethod
    def ganti_rintangan ():
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
           

    def buat_rintangan (self,evo):
        for rintangan in obstacles:
            rintangan.draw(screen)
            rintangan.update()
            if player1.gojo_rect.colliderect(rintangan.rect):
                    dead_sound = pygame.mixer.Sound('Music/Mati.ogg') 
                    dead_sound.play()
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
        self.rect.y = random.randint(380,500)
class Obstacle_pipa ():
    def update(self):
        self.rect.x -= speed
    def ganti_rintangan(self):
            x = random.randint(300 , 600)
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
                start_ptero(Score.hitung_score(self))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Powerup : 
    def __init__(self):
        self.image = powerup
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 350

    def power (self): 
        self.draw(screen)
        self.update()
     
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self):
        self.rect.x -= speed

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
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        return high_score

    def save_high_score(new_high_score):
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()


def pause():
    paused = True
    clock = pygame.time.Clock()
    screen.fill((255,255,255))
    # screen.blit(, (0, 0))
    # screen.blit("Pause",35, 1100/2, 836/2)
    # screen.blit("Tekan C Untuk Resume", 20, 1100/2, 836/2+70)
    # screen.blit("Tekan Q untuk keluar", 20, 1000/2, 836/2+97)
    pygame.display.update()

    clock.tick(speed)
    while paused:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()

def how_to_play():
    running = True
    while running: 
        pygame.display.set_mode((950,836))
        screen.fill((255,255,255))
        screen.blit(background_how_to,(0,0))

        if end_button.draw():
            start(0)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

def credits():
    running = True
    while running: 
        pygame.display.set_mode((950,836))
        screen.fill((255,255,255))
        screen.blit(background_credits,(0,0))

        if end_button.draw():
            start(0)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
   

def start_ptero(nilai):
    running = True
    while running:  
        pygame.display.set_mode((950,836))
        screen.fill((255,255,255))
        screen.blit(gameover_ptero,(0,0))
        if button_gameover_ptero.draw():
            pilih_karakter()
        if button_gameover_exit_ptero.draw():
            running = False
            pygame.quit()
            exit()
        score = font.render("Your Score: " + str(nilai), True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (470, 250+ 20)
        screen.blit(score, scoreRect)
        high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
        high_scoreRect = high_score.get_rect()
        high_scoreRect.center = (470, 250 )
        screen.blit(high_score, high_scoreRect)
        if nilai >Score.high_score():
            Score.save_high_score(nilai)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()


def pilih_karakter():
    running = True
    while running:
        screen.fill((225,225,255))
        screen.blit(background_select,(0,0))
        if dino_game.draw():
            pygame.mixer.music.load('Music/Background.ogg') 
            pygame.mixer.music.play(-1)
            game_dino()
        if ptero_game.draw():
            pygame.mixer.music.load('Music/Background.ogg') 
            pygame.mixer.music.play(-1)
            game_ptero()
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

def game_dino():
    pygame.display.set_mode((width,height))
    global poin, speed ,obstacles,player1,evo
    evo = False
    player1 = Dino()
    running = True 
    i = 0
    obstacles = []
    poin = 0
    speed = 15
    clock = pygame.time.Clock()
    score = Score()
    obstacle = Obstacle()
    power_up = Powerup()
    time  = 200
    tampilkan_powerup = False
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


        if poin >= 400  and poin % 500 == 0 or tampilkan_powerup == True  or user_input[pygame.K_9]:
            if evo == False:
                tampilkan_powerup = True
                power_up.power()
            if player1.gojo_rect.colliderect(power_up.rect):
                tampilkan_powerup = False
                evo = True
                power_up.rect.x = width
        if evo == True:
            time -= 1
            if time <= 0:
                evo = False
                time = 200

        player1.update(user_input,evo)
        Obstacle.ganti_rintangan()
        obstacle.buat_rintangan(evo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            elif user_input[pygame.K_p]:
                pause()
            
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
            user_input = pygame.key.get_pressed()
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
            if user_input[pygame.K_p]:
                pause()


def start (nilai):
    pygame.mixer.music.load('Music/Menu.ogg') 
    pygame.mixer.music.play()
    if nilai == 0: 
        running = True
        while running: 
            pygame.display.set_mode((950,836))
            screen.fill((255,255,255))
            screen.blit(background_menu,(0,0))
            if start_button.draw():
                pilih_karakter()
            if button_how_to.draw():
                how_to_play()
            if button_credits.draw():
                credits()
            if end_button.draw():
                running = False
                pygame.quit()
                exit()
            high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
            high_scoreRect = high_score.get_rect()
            high_scoreRect.center = (470, height // 2 - 50)
            screen.blit(high_score, high_scoreRect)
            if nilai >Score.high_score():
                Score.save_high_score(nilai)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
    elif evo == True:
        pass
    else: 
        running = True
        while running: 
            pygame.display.set_mode((950,836))
            screen.blit(gameover,(0,0))
            if button_gameover.draw():
                pilih_karakter()
            if button_gameover_exit.draw():
                running = False
                pygame.quit()
                exit()
            score = font.render("Your Score: " + str(nilai), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (470, 250+ 20)
            screen.blit(score, scoreRect)
            high_score = font.render("Your High Score: " + str(Score.high_score()), True, (0, 0, 0))
            high_scoreRect = high_score.get_rect()
            high_scoreRect.center = (470, 250 )
            screen.blit(high_score, high_scoreRect)
            if nilai >Score.high_score():
                Score.save_high_score(nilai)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    pygame.init()
    start(0)