import pygame
from gambar_Morphling import *

class Button: 
    def __init__(self, x , y ,image , scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.x = x
        self.y = y
        self.dino = True
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


#PILIHAN KARAKTER
#Tombol Start
button_start = pygame.image.load('Codingan Morphling/Gambarrr/Background/button_start.png')
start_button = Button(480,500,button_start,0.9)

#Tombol Exit
button_end = pygame.image.load('Codingan Morphling/Gambarrr/Background/exitt.png')
end_button = Button(480,600,button_end,0.9)

#Gambar Dino di pilihan karakter
x=0
game_dino = Gambar_Dino_Lari [ x % 8]
game_dino = pygame.transform.scale(game_dino,(150,150))
dino_game = Button(715,395,game_dino,1.15)

#Gambar Ptero di pilihan karakter
game_ptero = pygame.image.load('Codingan Morphling/Gambarrr/Ptero/pterodactyl5.png')
ptero_game = Button(200,400,game_ptero,1.5)


#PILIHAN KETIKA GAME OVER
#Tombol Play Again
gameover_button = pygame.image.load('Codingan Morphling/Gambarrr/Background/PlayAgain.png')
button_gameover = Button(480,600,gameover_button,0.20)

#Tombol Exit
gameover_button_exit = pygame.image.load('Codingan Morphling/Gambarrr/Background/button_exit.png')
button_gameover_exit = Button(480,680,gameover_button_exit,1.2)

#Gambar Dino mati
gameover = pygame.image.load('Codingan Morphling/Gambarrr/Background/gameover_dino.png')
gameover = pygame.transform.scale(gameover,(950,836))

#Gambar Ptero mati
gameover_ptero = pygame.image.load ('Codingan Morphling/Gambarrr/Background/gameover_ptero.png')
gameover_ptero = pygame.transform.scale(gameover_ptero,(950,836))