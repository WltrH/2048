
from select import POLLIN
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
                else:
                     matrice[i,j] = 0
    return (matrice)



#Mise en place de la fonction add_grid pour rajouter un élément dans la matrice (80% = 2 20% = 4)
    ########################################
    #     FONTION AJOUT CHIFFRE 2 ou 4     #
    ########################################

def add_digit(matrice):
    #création variables pour permettre l'extensibilité de la matrice
    lig = len(matrice[0])     #lignes
    col = len(matrice)  #colonnes

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
            #80% pour le chiffre 2 sinon 4
            if rand <= 8:
                matrice[li,co] = 2
                placed = True
            else :
                matrice[li,co] = 4
                placed = True
    return (matrice)



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
                matrice[i,j+1] = 0
                


def trollin(matrix, key):
    print("-----Matrice trollin-----")
    print (matrix)
    way = True

    
    while way :
        if key == ("g"):
            rolling_left(matrix)
            sum_digit(matrix)
            rolling_left(matrix)
            matrix = add_digit(matrix)
            print("-----Matrice trollin Gauche-----")
            print (matrix)
            return (matrix)
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
            return (matrix)
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
            return (matrix)
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
            return (matrix)
            way = False


def checkgame(matrice, state):
    lig = len(matrice[0])     #lignes
    col = len(matrice)  #colonnes
    while state:
        for i in range (lig):
            for j in range (col):
                if matrice[i,j] == 16:
                    state = False
                    print ("You won!")
                    return state
                else:
                    state = True
     




def game2048 ():
    #création matrice a 0
    #matrix = np.zeros((4,4))
    #initialisation matrice avec 2 valeurs de 2
    #matrix = init_grid()

    matrix = np.array([[2, 0, 2, 0],
                        [0, 2, 2, 0],
                        [0, 0, 8, 8],
                        [0, 0, 0, 0]])

    #booléen pour que le jeu se poursuive ou s'arrête s'il passe à False
    gaming = True

    print("lancement du jeux")
    print (matrix)
    #checkgame(matrix, gaming)

    while gaming == True:
            key = input("Veuillez choisir une direction enter h, b , d, g : ")
            trollin(matrix,key)
            gaming = checkgame(matrix, gaming)

    #contrôler que la matrice ne soit pas arrivée à 2048, sinon passer un message comme quoi le joueur à gagné



#Test des fonctions de mouvement du jeux
#matrice = np.zeros((4,4))
game2048()

"""
    matrice = np.array([[2, 0, 2, 0],
[0, 2, 2, 0],
[0, 0, 2, 2],
[0, 0, 0, 0]])

print ("-----Matrice de base-----")
print (matrice)

key = input ("Veuillez choisir en h, b, d, g: ")

trollin(matrice, key)

print ("-----Matrice après trollin------")
print (matrice)


"""


