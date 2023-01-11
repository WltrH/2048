
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
    lig = len(matrice)     #lignes
    col = len(matrice[0])  #colonnes

    #matrice = np.zeros((maxi,mini))
    values = [0,2]
    count = 0
    for i in range (lig):
        for j in range  (col):
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

    #booléen pour savoir si mon placement est juste
    placed = False

    #boucle while sur le bool tant que je suis à False je rentre dans la boucle
    while not placed:
        #Nombre random sur les lignes et colonnes pour avoir un emplacement
        li = np.random.randint(lig)
        co = np.random.randint(col)
        
        #si l'emplacement est = 0
        if matrice[li,co] == 0:
            #numéro random sur 10
            rand = np.random.randint(10)
        
            if rand <= 7:
                matrice[li,co] = 2
                placed = True
            else :
                matrice[li,co] = 4
                placed = True



#Mise en place de la fonction rolling_row pour faire l'addition des nombres dans la matrice avec ajout d'un numéro 
#venant de add_digit au dessus

def rolling_left(row):

    lig = len(matrice[0])     #lignes
    col = len(matrice)  #colonnes

    #si la variable row = 1 on fait passer les numéros de la matrice vers la gauche
    #faire en suite d'autres fonctions de déplacement pour ne laisser que cette fonction qui appelera les autres fonctions de mouvement

    if row == 1: #1 vaut déplacement sur la gauche
        for i in range (lig):
            for j in range (col):
                if matrice[i,j] != 0:
                    k = j
                    while k > 0 and matrice[i,k-1]==0:
                        matrice[i,k-1] = matrice[i,k]
                        matrice[i,k] = 0
                        k -= 1
# Fonction pour renvoyer les éléments de la matrice vers la droite 
def rolling_right(row):
    lig = len(matrice[0])     #lignes
    col = len(matrice)  #colonnes

   #2 vaut déplacement sur la droite 
    if row == 2: 

        #boucle pour les colonne
        for i in range (lig):
            for j in range (col):
                if matrice[i,j] != 0:
                    k = j
                    while k < col-1 and matrice[i,k+1]==0:
                        matrice[i,k+1] = matrice[i,k]
                        matrice[i,k] = 0
                        k += 1

                      
def rolling_up(row):

    lig = len(matrice)     #lignes
    col = len(matrice[0])  #colonnes
    
    if row == 3: #3 vaut déplacement vers le haut
        for i in range (col):
            for j in range (lig):
                if matrice[i,j] != 0:
                    l = i
                    while l > 0 and matrice[l-1,j]==0:
                        matrice[l-1,j] = matrice[l,j]
                        matrice[l,j] = 0
                        l -= 1

def rolling_down(row):

    lig = len(matrice)     #lignes
    col = len(matrice[0])  #colonnes
    
    if row == 4: #4 vaut déplacement vers le bas
        for i in range (col):
            for j in range (lig):
                if matrice[i,j] != 0:
                    l = i
                    while l < lig-1 and matrice[l+1,j]==0:
                        matrice[l+1,j] = matrice[l,j]
                        matrice[l,j] = 0
                        l += 1

def sum_digit(matrice):#pour la gauche

    lig = len(matrice)     #lignes
    col = len(matrice[0])  #colonnes

    for i in range (lig):
        for j in range (col-1):
            if matrice[i,j] == matrice[i,j+1]:
                matrice[i,j] = matrice[i,j] + matrice[i,j+1]
                matrice[i,j+1] = 0


matrice = np.zeros((4,4))
row = 1
#matrice = [[2, 2, 0, 0],[0, 0, 0, 0],[0, 0, 0, 2],[0, 0, 0, 0]]
print("---------------------")
print("---------------------")
init_grid(matrice)
print (matrice)
print("---------------------")
print("---------------------")
add_digit(matrice)
print (matrice)
print("---------------------")
print("---------------------")
rolling_left(row)
print(matrice)
print("--------gauche-------------")
print("---------------------")
sum_digit(matrice)
print(matrice)
print("---------droite------------")
print("---------------------")
row = 2
rolling_right(row)
print(matrice)
print("--------haut-------------")
print("---------------------")

row = 3
rolling_up(row)
print(matrice)
print("--------bas-------------")
print("---------------------")
row = 4
rolling_down(row)
print(matrice)
print("---------------------")
print("---------------------")
