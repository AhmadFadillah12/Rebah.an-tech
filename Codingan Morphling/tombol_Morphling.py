import pygame

from gambar_Morphling import *

class Button: 
    def __init__(self, x , y ,image , scale):
        self.__width = image.get_width()
        self.__height = image.get_height()
        self.__x = x
        self.__y = y
        self.__x_s = x
        self.__y_s = y
        self.image = pygame.transform.scale(image, (int(self.__width * scale) , int(self.__height * scale)))
        self.rect = self.image.get_rect(center=(self.__x, self.__y))
        self.clicked = False
        self.__count=0

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.__count<3:
                self.__x+=1
                self.__y+=1
                self.rect = self.image.get_rect(center=(self.__x, self.__y))
                self.__count+=1
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.__x = self.__x_s
            self.__y = self.__y_s
            self.rect = self.image.get_rect(center=(self.__x_s, self.__y_s))
            self.__count = 0

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