import pygame
import random

from gambar_Morphling   import *
from tombol_Morphling   import *
from karakter_Morphling import *
from gambar_Morphling   import *

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


        if poin > 400  and poin % 100 == 0 or tampilkan_powerup == True  or user_input[pygame.K_9]:
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
