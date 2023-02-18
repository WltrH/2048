import pygame
#import numpy as np
import Fonctions as fc
#from Fonctions import score

BG_COLORS = {
    0: (250, 250, 250),
    2: (238, 228, 218),
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 100),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 98),
    512: (237, 201, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

class Game2048:

    def __init__(self) ->None:
        self.N = 4
        self.taille = 100
        self.gap = 5
        self.couleur = (187, 173, 160)
        self.blocksize = self.taille + self.gap * 2

        self.hauteur = self.blocksize * 4
        self.largeur = self.hauteur
        global score
        score = 0

        pygame.init()

        #création de la fenêtre de jeu
        self.fenetre = pygame.display.set_mode((self.hauteur, self.largeur))
        pygame.display.set_caption("2048")

        #initialisation de la fenêtre
        self.fenetrestatus = fc.init_grid(self.N)
        self.fenetrestatus = fc.add_digit(self.fenetrestatus)
        
        

    #Création de rectangle
    def drawboard(self):
        self.fenetre.fill(self.couleur)

        for i in range (self.N):
            axeX = self.blocksize * i + self.gap
            for j in range (self.N):
                axeY = self.blocksize * j +self.gap
                cellValue = int(self.fenetrestatus[i][j])

                pygame.draw.rect(
                    self.fenetre,
                    BG_COLORS[cellValue], #mise de la couleur des cellules
                    pygame.Rect(axeX, axeY, self.taille, self.taille)
                )

    #Fonction pour le jeux
    def playing (self):

        statistiques = {}
        statistiques["Droite"] = 0
        statistiques["Haut"] = 0
        statistiques["Gauche"] = 0
        statistiques["Bas"] = 0
        global score
        score = 0
        
        run = True
        while run:
            self.drawboard()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print ('u')
                        key = 'h'
                        #statistiques = fc.statis(self.fenetrestatus, key)
                        self.fenetrestatus = fc.trollin(self.fenetrestatus, key)
                    elif event.key == pygame.K_DOWN:
                        print ('d')
                        key ='b'
                        #statistiques = fc.statis(self.fenetrestatus, key)
                        self.fenetrestatus = fc.trollin(self.fenetrestatus, key)
                    elif event.key == pygame.K_RIGHT:
                        print ('r')
                        key='d'
                        #statistiques = fc.statis(self.fenetrestatus, key)
                        self.fenetrestatus = fc.trollin(self.fenetrestatus, key)
                    elif event.key == pygame.K_LEFT:
                        print('l')
                        key = 'g'
                        #statistiques = fc.statis(self.fenetrestatus, key)
                        self.fenetrestatus = fc.trollin(self.fenetrestatus, key)
                    elif event.key == pygame.K_ESCAPE:
                        running = False


if __name__ == "__main__":
    game = Game2048()
    game.playing()







