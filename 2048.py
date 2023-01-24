
from select import POLLIN
import matplotlib.pyplot as plt
import numpy as np
import random

#initialisation de la matrice por le jeux 2048
#matrice extensible
    ########################################
    #     INITIALISATION DE LA MATRICE     #
    ########################################
def init_grid ():

    #création de la matrice
    matrice = np.zeros((4,4))

    #création variables pour permettre l'extensibilité de la matrice
    lig = len(matrice[0])     #lignes
    col = len(matrice)  #colonnes

    values = [0,2]
    count = 0
    for i in range (lig):
        for j in range  (col):
            #mise des valeurs à 0 et 2 avec un maximum de 2 valeurs à 2 et le reste à 0
            if count < 2: 
                matrice[i,j] = np.random.choice(values)
                if matrice[i,j] == 2:
                    count += 1
    return (matrice)



#Mise en place de la fonction add_grid pour rajouter un élément dans la matrice (80% = 2 20% = 4)
    ########################################
    #     FONTION AJOUT CHIFFRE 2 ou 4     #
    ########################################

def add_digit(matrice):
    
    lig = len(matrice[0])     #lignes
    col = len(matrice)  #colonnes
    count = 0
    placed = False
    for i in range (lig):
        for j in range (col):
            if matrice[i,j] == 0:
                count +=1
    if count == 0:
        return matrice
    else:
        li = np.random.randint(lig)
        co = np.random.randint(col)
        while matrice[li,co] != 0:
            li = np.random.randint(lig)
            co = np.random.randint(col)
        rand = np.random.randint(10)
        if rand <= 8:
            matrice[li,co] = 2
        else :
            matrice[li,co] = 4
    return matrice




#Mise en place de la fonction rolling_row pour faire l'addition des nombres dans la matrice avec ajout d'un numéro 
#venant de add_digit au dessus

    ########################################
    #   FONTION DECALAGE VERS LA GAUCHE    #
    ########################################

def rolling_left(matrice):

    lig = len(matrice[0])     #lignes
    col = len(matrice)  #colonnes

    #si la variable row = 1 on fait passer les numéros de la matrice vers la gauche
    #faire en suite d'autres fonctions de déplacement pour ne laisser que cette fonction qui appelera les autres fonctions de mouvement

    for i in range (lig):
        for j in range (col):
            if matrice[i,j] != 0:
                k = j
                while k > 0 and matrice[i,k-1]==0:
                    matrice[i,k-1] = matrice[i,k]
                    matrice[i,k] = 0
                    k -= 1
    return (matrice)

    ########################################
    #           FONTION ADDITION           #
    ########################################

def sum_digit(matrice):#pour la gauche

    lig = len(matrice)     #lignes
    col = len(matrice[0])  #colonnes


    for i in range (lig):
        for j in range (col-1):
            if matrice[i,j] == matrice[i,j+1]:
                matrice[i,j] = matrice[i,j] + matrice[i,j+1]
                #add_number.append(matrice[i,j] + matrice[i,j+1])
                matrice[i,j+1] = 0
    return (matrice)

    ########################################
    #           FONTION TROLLIN            #
    ########################################

def trollin(matrix, key, copy=False):
    print("-----Matrice trollin-----")
    print (matrix)
    way = True
    
    if copy:
        matrix = matrix.copy()
    
    while way :
        if key == ("g"):
            rolling_left(matrix)
            sum_digit(matrix)
            rolling_left(matrix)
            matrix = add_digit(matrix)
            print("-----Matrice trollin Gauche-----")
            print (matrix)
            way = False

        elif key ==("d"):
            matrix = np.rot90(matrix, k = -2)
            print("-----Matrice trollin rotation-----")
            print (matrix)
            rolling_left(matrix)
            sum_digit(matrix)
            rolling_left(matrix)
            matrix = np.rot90(matrix,k = 2)
            matrix = add_digit(matrix)
            print("-----Matrice trollin Droite-----")
            print (matrix)
            way = False

        elif key ==("h"):
            matrix = np.rot90(matrix, k = -3)
            print("-----Matrice trollin rotation-----")
            print (matrix)
            rolling_left(matrix)
            sum_digit(matrix)
            rolling_left(matrix)
            matrix = np.rot90(matrix,k = 3)
            matrix = add_digit(matrix)
            print("-----Matrice trollin Haut-----")
            print (matrix)
            way = False

        elif key == ("b"):
            matrix = np.rot90(matrix, k = -1)
            rolling_left(matrix)
            sum_digit(matrix)
            rolling_left(matrix)
            matrix = np.rot90(matrix,k = 1)
            matrix = add_digit(matrix)
            print("-----Matrice trollin Bas-----")
            print (matrix)
            way = False
           
    return (matrix)        

    ########################################
    #   FONTION VERIFICATION ETAT DU JEU   #
    ########################################

def checkgameover(matrice):
    lig = len(matrice[0])     #lignes
    col = len(matrice)  #colonnes

    if checkmatricemove(matrice) == True:
        return False

    for i in range (lig):
        for j in range (col):
            if matrice[i,j] == 16:
                print ("You won!")
                return True
    return (False)


    ########################################
    #    FONTION VERIFICATION MOUVEMENT    #
    ########################################
def checkmatricemove(matrice):
    #doit dire si la matrice est identique après avoir essayer de bouger dans les 4 directions
    lig = len(matrice)     #lignes
    col = len(matrice[0])  #colonnes

# vérifie s'il existe une case vide dans la matrice
    for i in range(lig):
        for j in range(col):
            if matrice[i, j] == 0:
                return False

# vérifie s'il existe des cases identiques côte à côte
    for i in range(lig):
        for j in range(col - 1):
            if matrice[i, j] == matrice[i, j + 1]:
                return False
    for i in range(lig - 1):
        for j in range(col):
            if matrice[i, j] == matrice[i + 1, j]:
                return False

# s'il n'y a ni case vide ni cases identiques côte à côte, aucun mouvement valide n'est possible
    return True


    ########################################
    #               STATS                    #
    ########################################
def affstats (values):
    #Tentatvie camenbert 
    x = []
    y = []
    explode = (0, 0.1, 0, 0)

    for k, v in values.items():
        x.append(k)
        y.append(v)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(y, explode = explode, labels= x, autopct='%1.1f%%',
            shadow = True, startangle = 90)
    fig1.canvas.manager.set_window_title('Statistiques 2048')

    plt.title('Pourcentage Direction')
    # Affiche le graphique
    plt.show()


def statis(stats, key):
    #recherche avec le clef pour mettre +1
    if key == "d":
         stats["Droite"] = stats.get("Droite", 0) + 1
    if key == "h":
        stats["Haut"] = stats.get("Haut", 0) + 1
    if key == "g":
        stats["Gauche"] = stats.get("Gauche", 0) + 1
    if key == "b":
        stats["Bas"] = stats.get("Bas", 0) + 1
    return stats




    ########################################
    #               JEU                    #
    ########################################
def game2048 ():
    #création matrice a 0
    matrix = np.zeros((4,4))
    #initialisation matrice avec 2 valeurs de 2
    matrix = init_grid()
    #booléen pour que le jeu se poursuive ou s'arrête s'il passe à False
    gaming = False
    #tableau des scores
    #add_number = []
    stats = {}
    stats["Droite"] = 0
    stats["Haut"] = 0
    stats["Gauche"] = 0
    stats["Bas"] = 0



    print("lancement du jeux")
    print (matrix)
    #checkgame(matrix, gaming)
    #gaming = checkmatricemove(matrix)
    while not gaming:
            key = input("Veuillez choisir une direction enter h, b , d, g : ")
            statis(stats, key)
            trollin(matrix,key)
            gaming = checkgameover(matrix)
            #print(values)
    
    print (stats)
    key = input("Affichier les stats ? : y,n ")
    if key == "y":
        affstats(stats)
    
            

    #contrôler que la matrice ne soit pas arrivée à 2048, sinon passer un message comme quoi le joueur à gagné


game2048()


#Test des fonctions de mouvement du jeux
#matrice = np.zeros((4,4))
