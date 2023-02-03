import pygame
#import numpy as np
import Fonctions as fc


class Game2048:

    def __init__(self) ->None:
        self.N = 4
        self.taille = 100
        self.gap = 5
        self.couleur = (187, 173, 160)
        self.blocksize = self.taille + self.gap * 2

        self.hauteur = self.blocksize * 4
        self.largeur = self.hauteur

        pygame.init()

        #création de la fenêtre de jeu
        self.fenetre = pygame.display.set_mode((self.hauteur, self.largeur))
        pygame.display.set_caption("2048")

        #initialisation de la fenêtre
        self.fenetreStart = fc.init_grid(self.N)
        self.addNumber = fc.add_digit(self.fenetreStart)

    #Création de rectangle
    def drawboard(self):
        self.fenetre.fill(self.couleur)

        for i in range (self.N):
            axeX = self.blocksize * i + self.gap
            for j in range (self.N):
                axeY = self.blocksize * j +self.gap

                pygame.draw.rect(
                    self.fenetre,
                    (0,0,0), #mise de la couleur des cellules
                    pygame.Rect(axeX, axeY, self.taille, self.taille)
                )

    #Fonction pour le jeux
    def playing (self):

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
                    elif event.key == pygame.K_DOWN:
                        print ('d')
                    elif event.key == pygame.K_RIGHT:
                        print ('r')
                    elif event.key == pygame.K_LEFT:
                        print('l')
                    elif event.key == pygame.K_ESCAPE:
                        running = False


if __name__ == "__main__":
    game = Game2048()
    game.playing()






