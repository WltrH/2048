import pygame
import Fonctions 


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

    def drawboard(self):
        self.fenetre.fill(self.couleur)

        for i in self.N:
            axeX = self.blocksize * i + self.gap
            for j in self.N:
                axeY = self.blocksize * j +self.gap

                pygame.draw.rect(
                    self.hauteur,
                    (0,0,0),
                    pygame.rect(axeX, axeY, self.taille, self.taille)
                )

    def playing (self):

        run = True
        while run:
            self.drawboard()
            pygame.display.update()

if __name__ == "__main__":
    game = Game2048()
    game.playing()






