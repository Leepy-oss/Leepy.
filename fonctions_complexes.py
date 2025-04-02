#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      victorantoine
#
# Created:     07/02/2025
# Copyright:   (c) victorantoine 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from classe_complexe import *
from math import *

################################################################################


def points_complexes_plan(L:list):
    '''Fonction qui trace un nuage de points dans un plan complexe
     selon une liste d'affixes respectifs de ces points'''
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.xlabel('Axe des Réels')
    plt.ylabel('Axe des Imaginaires')
    plt.grid(True, linestyle='--', linewidth=0.5)
    for elem in L:
        x = elem.get_partieReelle()
        y = elem.get_partieImaginaire()
        plt.plot(x,y, 'bo')
        plt.annotate(elem.get_nom(),(x,y),textcoords="offset points", xytext=(0,10), ha='center')
    plt.title("Plan Complexe")
    plt.show()


def points_complexes_espace(L:list):
    '''Fonction qui projete un nuage de points du plan complexe dans l'espace
    avec un deuxieme axe des réels'''
    ax = plt.axes(projection = '3d')
    ax.set_xlabel('Axe des Réels')
    ax.set_ylabel('Axe des Imaginaires')
    ax.set_zlabel('Axe des Réels')
    for elem in L:
        x = elem.get_partieReelle()
        y = elem.get_partieImaginaire()
        z = x
        ax.scatter(x,y,z, c= 'red')
        ax.text(x,y,z,elem.get_nom(),color = 'black')
    ax.set_title("'Espace Complexe'")
    plt.show()




#------------------------------------------------------------------------------>


def produit_complexes_plan(z1,z2):
    '''Fonction qui fait le produit de deux nombres complexes et affiche sous forme de nuage de points dans le plan complexe,
    le point dont l'affixe est donné par le produit et les points dont leurs affixes sont multipliés'''
    L=[z1,z2]
    z3 = Complexe("Z")
    z3.set_partieReelle((z1.get_partieReelle()*z2.get_partieReelle())-(z1.get_partieImaginaire()*z2.get_partieImaginaire()))
    z3.set_partieImaginaire((z1.get_partieReelle()*z2.get_partieImaginaire())+(z1.get_partieImaginaire()*z2.get_partieReelle()))
    L.append(z3)
    print(z3)
    points_complexes_plan(L)


def produit_complexes_espace(z1,z2):
    '''Fonction qui fait le produit de deux nombres complexes et affiche sous forme de nuage de points dans "l'espace complexe",
    le point dont l'affixe est donné par le produit et les points dont leurs affixes sont multipliés'''
    L=[z1,z2]
    z3 = Complexe("Z")
    z3.set_partieReelle((z1.get_partieReelle()*z2.get_partieReelle())-(z1.get_partieImaginaire()*z2.get_partieImaginaire()))
    z3.set_partieImaginaire((z1.get_partieReelle()*z2.get_partieImaginaire())+(z1.get_partieImaginaire()*z2.get_partieReelle()))
    L.append(z3)
    points_complexes_espace(L)
    print(z3)


##z1 = Complexe("z1",1,-sqrt(3))
##z2 = Complexe("z2",1,sqrt(3))
##z3 = Complexe("z3",7,0)
##z4 = Complexe("z4",0,2)
##L=[z1,z2,z3,z4]



#------------------------------------------------------------------------------>




