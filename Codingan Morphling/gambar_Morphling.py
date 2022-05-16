import pygame


#Ukuran Window
width = 1100
height = 836
screen = pygame.display.set_mode((width,height))
font = pygame.font.Font('freesansbold.ttf',20)
pygame.display.set_caption ("Morphling")
icon = pygame.image.load ('Codingan Morphling/Gambarrr/pterodactyl.png')
pygame.display.set_icon(icon)

#Background Ptero
background_ptero = pygame.image.load('Codingan Morphling/Gambarrr/FinalNight1.png')
background_ptero = pygame.transform.scale(background_ptero,(875,936))

#Gambar Karakter
Gambar_Dino_Awal   =    pygame.image.load('Codingan Morphling/Gambarrr/dino_idle.png')
Gambar_Dino_Nunduk =   [pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Nunduk/Proses Nunduk1.png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Nunduk/Proses Nunduk2.png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Nunduk/Proses Nunduk3.png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Dino Nunduk/Proses Nunduk4.png'),]
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

Gambar_Dino_Awal_evo   =    pygame.image.load('Codingan Morphling/Gambarrr/dino_idle.png')
Gambar_Dino_Nunduk_evo =   [pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Nunduk/Proses Nunduk1.png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Nunduk/Proses Nunduk2.png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Nunduk/Proses Nunduk3.png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Nunduk/Proses Nunduk4.png'),]
Gambar_Dino_Lari_evo   =   [pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lari/Run (1).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lari/Run (2).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lari/Run (3).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lari/Run (4).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lari/Run (5).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lari/Run (6).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lari/Run (7).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lari/Run (8).png')]
Gambar_Dino_Melompat_evo = [pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (1).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (2).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (3).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (4).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (5).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (6).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (7).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (8).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (9).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (10).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (11).png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Dino/Evolusi/Dino Lompat/Jump (12).png')]

Gambar_Obstacle_Batu = [pygame.image.load('Codingan Morphling/Gambarrr/Batu/Crystal2.png'),
                        pygame.image.load('Codingan Morphling/Gambarrr/Batu/Crystal4.png')]
Gambar_Ptero = [pygame.image.load('Codingan Morphling/Gambarrr/Ptero/Pterodactyl1.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/Pterodactyl2.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/Pterodactyl3.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/Pterodactyl4.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/Pterodactyl5.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/Pterodactyl6.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/Pterodactyl7.png'),
                pygame.image.load('Codingan Morphling/Gambarrr/Ptero/Pterodactyl8.png'),]


#Gambar Obstacle Ptero
pipa = pygame.image.load('Codingan Morphling/Gambarrr/Pipa/pipa 1.png')
pipa = pygame.transform.flip(pipa, False, True)
pipaatas = pygame.image.load('Codingan Morphling/Gambarrr/Pipa/pipa 2.png')
pipa = pygame.transform.scale(pipa, (80, 380))
pipaatas = pygame.transform.scale(pipaatas, (110, 380))

#Gambar Obstacle Dino
Gambar_Obstacle_Batu[0] = pygame.transform.scale(Gambar_Obstacle_Batu[0],(90,90))
Gambar_Obstacle_Batu[1] = pygame.transform.scale(Gambar_Obstacle_Batu[1],(90,90))
pohon = pygame.image.load('Codingan Morphling/Gambarrr/Pohon/7.png')
pohon = pygame.transform.scale(pohon, (90, 130))
bird = pygame.image.load('Codingan Morphling/Gambarrr/seagull.png')
bird = pygame.transform.scale(bird, (70, 70))
pohonbesar = pygame.image.load('Codingan Morphling/Gambarrr/Pohon/1.png')
pohonbesar = pygame.transform.scale(pohonbesar, (110, 120))
powerup = pygame.image.load('Codingan Morphling/Gambarrr/Powerup/powerup.png')
powerup = pygame.transform.scale(powerup, (70, 70))

#Background memilih karakter   
background_select = pygame.image.load('Codingan Morphling/Gambarrr/Background/character_select.jpeg')
background_select = pygame.transform.scale(background_select,(950,836))

#Background Menu Game
background_menu = pygame.image.load('Codingan Morphling/Gambarrr/menu_start.png')
background_menu = pygame.transform.scale(background_menu,(950,836)) 

#Background Dino
background = pygame.image.load('Codingan Morphling/Gambarrr/background.png')
background = pygame.transform.scale(background,(width,height))