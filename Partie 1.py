# %%
from turtle import color
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from collections import Counter


def marche1(n):
    pos = 0
    x = [k for k in range(n+1)]
    axeabsisse = [0 for k in range(n+1)]
    result = []
    result.append(pos)
    for i in range(0, n):
        rdm = random.uniform(0, 1)
        if rdm < 0.5:
            pos += 1
        else:
            pos += -1
        result.append(pos)
    plt.title("Simulation marche aléatoire 1D avec n = " + str(n))
    plt.plot(x, result, label="Position à l'instant k")
    plt.plot(x, axeabsisse, label="position x=0")
    plt.legend()
    plt.grid()
    
marche1(4)
#%% 

#-----------------Histogramme-----------------
def marche1(n):
    pos = 0
    for i in range(0,n):
        rdm = random.uniform(0, 1)
        if rdm<0.5:
            pos += 1
        else :
            pos += -1
    return pos

def histogramme1D(Ntot, n):
    Xn = []
    for i in range (Ntot):
        Xn.append(marche1(n))
    Liste = Counter(Xn).most_common() #Permet d'obtenir un tableau à partir d'un autre en comptant les occurences
                                    # Exemple : tableau 1 : [1,0,0,3] , tableau 2 en sortie : [(0,2),(3,1),(1,1)]
                                    # On a (0,2) puisque l'on a 2x la valeur 0 dans le tableau 1
    x = []
    y = []
    for i in Liste:
        x.append(i[0]) #on récupère toutes les positions finales
        y.append(i[1]) 

    fig, axs = plt.subplots(1, 1,
                            figsize =(10, 7),
                            tight_layout = True)

    plt.hist(Xn, len(y))
    # Setting color
    N, bins, patches = axs.hist(Xn, bins = len(y))
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())
    
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
        
    # Adding extra features   
    plt.xlabel("Position")
    plt.ylabel("Fréquence")
    plt.title("Histogramme des positions finales obtenues pour n = " 
              + str(n) + " pour "+ str(Ntot)+" marches simulées")
    
    # Show plot
    plt.show()
    print(Liste)

Ntot = 100000
n = 100
histogramme1D(Ntot,n)

#%%
#-----------------Retour à 0-----------------

def marche1_retour_à_0(n):
    print("nv it")
    print()
    pos = 0
    nb = 0
    for i in range(0,n):
        rdm = random.uniform(0, 1)
        if rdm<0.5:
            pos += 1
        else :
            pos += -1
        print(pos)
        if pos == 0 :
            nb = 1
        print("nb = "+ str(nb))
    return nb

def histogramme1D_retour_à_0(Ntot, n):
    Xn = []
    for i in range (Ntot):
        Xn.append(marche1_retour_à_0(n))
    Liste = Counter(Xn).most_common() #Permet d'obtenir un tableau à partir d'un autre en comptant les occurences
                                    # Exemple : tableau 1 : [1,0,0,3] , tableau 2 en sortie : [(0,2),(3,1),(1,1)]
                                    # On a (0,2) puisque l'on a 2x la valeur 0 dans le tableau 1
    x = []
    y = []
    for i in Liste:
        x.append(i[0]) #on récupère toutes les positions finales
        y.append(i[1]) 

    fig, axs = plt.subplots(1, 1,
                            figsize =(10, 7),
                            tight_layout = True)

    plt.hist(Xn, len(y))
    # Setting color
    N, bins, patches = axs.hist(Xn, bins = len(y))
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())
    
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
        
    # Adding extra features   
    plt.xlabel("Position")
    plt.ylabel("Fréquence")
    plt.title("Histogramme des marches passant au moins une fois à 0 pour n = " 
              + str(n) + " pour "+ str(Ntot)+" marches simulées")
    
    # Show plot
    plt.show()
    print(Liste)

Ntot = 10
n = 5
histogramme1D_retour_à_0(Ntot,n)
# %%
# DQOQSIO