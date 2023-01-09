
import numpy as np
import random

"""
1-Commencez par définir la structure de votre grille de jeu. Vous pouvez utiliser 
une liste à double entrée pour stocker les valeurs de chaque case de la grille.

2-Ensuite, écrivez une fonction qui gère les déplacements de la grille lorsque 
l'utilisateur utilise les flèches du clavier. Cette fonction devra prendre en compte les règles du jeu, 
comme la fusion de cases de même valeur et l'interdiction de déplacer des cases vers des cases déjà occupées.

3-Ajoutez une fonction qui gère l'ajout de nouvelles cases à la grille après chaque coup joué par l'utilisateur. 
Cette fonction devra choisir au hasard une case vide et y insérer une nouvelle valeur (2 ou 4).

4-Enfin, écrivez une fonction principale qui initialise la grille et gère les entrées de l'utilisateur jusqu'à ce que la partie
 soit terminée (soit parce que la grille est pleine, soit parce que l'utilisateur a atteint la valeur cible 2048).

Je vous recommande également d'utiliser la bibliothèque pygame pour gérer l'interface graphique de votre jeu. 
Cela vous permettra de créer une grille affichée à l'écran et de gérer les entrées de l'utilisateur à l'aide de la bibliothèque pygame.
test ster
"""


#initialisation de la matrice por le jeux 2048

#matrice extensible


def init_grid (matrice):

    #création variables pour permettre l'extensibilité de la matrice
    maxi = len(matrice)     #lignes
    mini = len(matrice[0])  #colonnes

    #matrice = np.zeros((maxi,mini))
    values = [0,2]
    count = 0
    for i in range (maxi):
        for j in range  (mini):
            #mise des valeurs à 0 et 2 avec un maximum de 2 valeurs à 2 et le reste à 0
            if count < 2: 
                matrice[i][j] = np.random.choice(values)
                if matrice[i][j] == 2:
                    count += 1
                else:
                     matrice[i][j] = 0


#MMise en place de la fonction add_grid pour rajouter un élément dans la matrice (80% = 2 20% = 4)

def add_digit(matrice):
    #création variables pour permettre l'extensibilité de la matrice
    lig = len(matrice)     #lignes
    col = len(matrice[0])  #colonnes

    placed = False

    print("----------Placed-----------")
    print (placed)

    while not placed:
        li = np.random.randint(lig)
        co = np.random.randint(col)
        print("----------li&co-----------")
        print (li, co)
        

        if matrice[li,co] == 0:
            rand = np.random.randint(10)
        
            if rand <= 7:
                matrice[li,co] = 2
                placed = True
            else :
                matrice[li,co] = 4
                placed = True



matrice = np.zeros((4,4))
print("---------------------")
print("---------------------")
init_grid(matrice)
print (matrice)
print("---------------------")
print("---------------------")
add_digit(matrice)
print (matrice)
 