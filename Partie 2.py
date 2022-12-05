# %%
from turtle import color
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import statistics as st
from collections import Counter

# %% Questions 2/3 TODO: ici on voit des mouvement browniens
# -------------------- Marche aléatoire 2D


def marche2(n):
    # Initialisation des variables
    posX = 0
    posY = 0
    size = 2
    temp = []
    resultX = []
    resultY = []
    resultXdr = []
    resultYdr = []
    resultX.append(posX)
    resultY.append(posY)

    # Pour n pas
    for i in range(1, n+1):
        # On choisit d'avancer dans une direction aléatoire
        rdm = random.uniform(0, 1)
        if rdm <= 0.25:
            posX += 1
        elif (rdm <= 0.5) & (rdm > 0.25):
            posX += -1
        elif (rdm <= 0.75) & (rdm > 0.5):
            posY += 1
        else:
            posY += -1

        resultX.append(posX)
        resultY.append(posY)

        # Afin d'avoir un gradient pour mieux visualiser le sens de progression
        # on crée 100 points entre chaques pas, ces points seront colorés via une colorscale
        if resultX[i] != resultX[i-1]:
            if resultX[i] > resultX[i-1]:
                temp = np.arange(resultX[i-1], resultX[i], 0.01)
            if resultX[i] < resultX[i-1]:
                temp = np.arange(resultX[i-1], resultX[i], -0.01)
            for j in range(0, 99):
                resultXdr.append(temp[j])
                resultYdr.append(resultY[i])
            temp = []
        if resultY[i] != resultY[i-1]:
            if resultY[i] > resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], 0.01)
            if resultY[i] < resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], -0.01)
            for j in range(0, 99):
                resultYdr.append(temp[j])
                resultXdr.append(resultX[i])
            temp = []

    # On modifie la largeur du trait
    if n > 500:
        size = 1
    elif n > 2000:
        size = 0.5
    elif n > 6000:
        size = 0.01

    # Traçage de la courbe (en fait une série de points)
    color = [k for k in range(len(resultXdr))]
    plt.title("Marche aléatoire 2D avec n = " + str(n))
    plt.scatter(resultXdr, resultYdr, c=color, cmap='Spectral', s=size)
    plt.locator_params(axis='both', nbins=6)
    plt.axis('square')
    plt.grid()
    plt.show()


marche2(500)


# -------------------- Marche aléatoire 2D sans retour en arrière


def marche2SR(n):
    posX = 0
    posY = 0
    size = 2
    done = False
    addX = False
    subX = False
    addY = False
    subY = False
    temp = []
    resultX = []
    resultY = []
    resultXdr = []
    resultYdr = []
    resultX.append(posX)
    resultY.append(posY)

    # Pour le premier pas toutes les directions sont autorisées
    rdm = random.uniform(0, 1)
    if rdm <= 0.25:
        addX = True
    elif (rdm <= 0.5) & (rdm > 0.25):
        subX = True
    elif (rdm <= 0.75) & (rdm > 0.5):
        addY = True
    else:
        subY = True

    # Il faut ensutie choisir avec une meme probabilité une direction
    # qu'y ne fait pas retourner en arrière
    for i in range(1, n+1):
        rdm = random.uniform(0, 1)
        if (addX == True) & (done == False):
            if rdm <= 1/3:
                posX += 1
                addX = False
                addX = True
            elif (rdm <= 2/3) & (rdm > 1/3):
                posY += 1
                addX = False
                addY = True
            else:
                posY += -1
                addX = False
                subY = True
            done = True
        if (subX == True) & (done == False):
            if rdm <= 1/3:
                posX += -1
                subX = False
                subX = True
            elif (rdm <= 2/3) & (rdm > 1/3):
                posY += 1
                subX = False
                addY = True
            else:
                posY += -1
                subX = False
                subY = True
            done = True
        if (addY == True) & (done == False):
            if rdm <= 1/3:
                posX += 1
                addY = False
                addX = True
            elif (rdm <= 2/3) & (rdm > 1/3):
                posY += 1
                addY = False
                addY = True
            else:
                posX += -1
                addY = False
                subX = True
            done = True
        if (subY == True) & (done == False):
            if rdm <= 1/3:
                posX += 1
                subY = False
                addX = True
            elif (rdm <= 2/3) & (rdm > 1/3):
                posX += -1
                subY = False
                subX = True
            else:
                posY += -1
                subY = False
                subY = True
            done = True
        done = False

        resultX.append(posX)
        resultY.append(posY)

        if resultX[i] != resultX[i-1]:
            if resultX[i] > resultX[i-1]:
                temp = np.arange(resultX[i-1], resultX[i], 0.01)
            if resultX[i] < resultX[i-1]:
                temp = np.arange(resultX[i-1], resultX[i], -0.01)
            for j in range(0, 99):
                resultXdr.append(temp[j])
                resultYdr.append(resultY[i])
            temp = []
        if resultY[i] != resultY[i-1]:
            if resultY[i] > resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], 0.01)
            if resultY[i] < resultY[i-1]:
                temp = np.arange(resultY[i-1], resultY[i], -0.01)
            for j in range(0, 99):
                resultYdr.append(temp[j])
                resultXdr.append(resultX[i])
            temp = []

    if n > 500:
        size = 1
    elif n > 2000:
        size = 0.5
    elif n > 6000:
        size = 0.01

    color = [k for k in range(len(resultXdr))]
    plt.title("Marche aléatoire 2D sans retour avec n = " + str(n))
    plt.scatter(resultXdr, resultYdr, c=color, cmap='Spectral', s=size)
    plt.locator_params(axis='both', nbins=6)
    plt.axis('square')
    plt.grid()
    plt.show()


marche2SR(100)


# %% Question 4
# -------------------- Distance moyenne à l'origine

def distance(n, nbsample):
    posX = 0
    posY = 0
    distance = []

    for i in range(0, nbsample):
        for j in range(1, n+1):
            rdm = random.uniform(0, 1)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            else:
                posY += -1

        # On stocke les distances à l'origine dans un tableau dont on pourra ensuite faire la moyenne
        distance.append(math.sqrt(posX * posX + posY * posY))
        # On place un point bleu sur chaque fin de parcours (Xn,Yn)
        plt.plot(posX, posY, marker="o", markersize=10,
                 markeredgecolor="blue", markerfacecolor="cyan")
        posX = 0
        posY = 0

    # On place un point rose à l'origine du repère
    plt.plot(0, 0, marker="o", markersize=10,
             markeredgecolor="red", markerfacecolor="purple")
    plt.title("Marche 2D avec n = " + str(n) +
              " et " + str(nbsample) + " répétitions")
    plt.grid()
    plt.locator_params(axis='both', nbins=6)
    plt.axis('square')
    plt.show()
    print("Pour n=", n, " la distance moyenne à l'origine est de ", st.mean(distance))


# distance(n,nbsample) avec n le nombre de pas et nbsample le nombre d'échantillons
# les points bleu représentent tout les points (Xn,Yn) et le rose l'origine
distance(1000, 1000)


# -------------------- Distance moyenne à l'origine sans retour en arrière

def distanceSR(n, nbsample):
    posX = 0
    posY = 0
    done = False
    addX = False
    subX = False
    addY = False
    subY = False
    distance = []

    for i in range(0, nbsample):
        rdm = random.uniform(0, 1)
        if rdm <= 0.25:
            addX = True
        elif (rdm <= 0.5) & (rdm > 0.25):
            subX = True
        elif (rdm <= 0.75) & (rdm > 0.5):
            addY = True
        else:
            subY = True

        for j in range(1, n+1):
            rdm = random.uniform(0, 1)
            if (addX == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addX = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addX = False
                    addY = True
                else:
                    posY += -1
                    addX = False
                    subY = True
                done = True
            if (subX == True) & (done == False):
                if rdm <= 1/3:
                    posX += -1
                    subX = False
                    subX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    subX = False
                    addY = True
                else:
                    posY += -1
                    subX = False
                    subY = True
                done = True
            if (addY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    addY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posY += 1
                    addY = False
                    addY = True
                else:
                    posX += -1
                    addY = False
                    subX = True
                done = True
            if (subY == True) & (done == False):
                if rdm <= 1/3:
                    posX += 1
                    subY = False
                    addX = True
                elif (rdm <= 2/3) & (rdm > 1/3):
                    posX += -1
                    subY = False
                    subX = True
                else:
                    posY += -1
                    subY = False
                    subY = True
                done = True
            done = False
        distance.append(math.sqrt(posX * posX + posY * posY))
        plt.plot(posX, posY, marker="o", markersize=10,
                 markeredgecolor="blue", markerfacecolor="cyan")
        posX = 0
        posY = 0

    plt.plot(0, 0, marker="o", markersize=10,
             markeredgecolor="red", markerfacecolor="purple")
    plt.title("Marche 2D sans retour avec n = " + str(n) +
              " et " + str(nbsample) + " répétitions")
    plt.grid()
    plt.locator_params(axis='both', nbins=6)
    plt.axis('square')
    plt.show()
    print("Pour n=", n, " la distance moyenne à l'origine est de ", st.mean(distance))


distanceSR(1000, 1000)
# %% Question 5
# -------------------- Probabilité de retour à (0,0)


def retour02D(n, nbsample):
    j = 0
    nb0 = 0
    posX = 0
    posY = 0
    retour0 = False

    for i in range(0, nbsample):
        # On arrète la boucle dès que le parcours passe par (0,0) pour réduire le temps d'éxecution
        while (j != n+1) & (retour0 == False):
            rdm = random.uniform(0, 1)
            if rdm <= 0.25:
                posX += 1
            elif (rdm <= 0.5) & (rdm > 0.25):
                posX += -1
            elif (rdm <= 0.75) & (rdm > 0.5):
                posY += 1
            else:
                posY += -1
            if (posX == 0) & (posY == 0):
                retour0 = True
                nb0 += 1
            j += 1
        retour0 = False
        posX = 0
        posY = 0
        j = 0

    print("On a un nombre de pas ", n)
    print("Nombre de retours à 0 pour ",
          nbsample, " marches aléatoires : ", nb0)
    print("Soit une probabilité de retourner à 0 de : ", round(nb0/nbsample, 3))


# distance(n,nbsample) avec n le nombre de pas et nbsample le nombre d'échantillons
# les points bleu représentent tout les points (Xn,Yn) et le rose l'origine
retour02D(10, 10000)
