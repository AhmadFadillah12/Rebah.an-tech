import pygame

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