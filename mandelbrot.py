#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      victorantoine
#
# Created:     28/03/2025
# Copyright:   (c) victorantoine 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
from classe_complexe import *
from math import *

def mandelbrot(c, max_iter=1000):
    z = c.get_complexe()
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z**2 + c.get_complexe()
    return max_iter

def ensembleMandelbrot(xmin, xmax, ymin, ymax, largeur, hauteur, max_iter=100):
    mandelbrot_image = np.ones((hauteur, largeur))
    for y in range(hauteur):
        for x in range(largeur):
            reel = xmin + (x / largeur) * (xmax - xmin)
            imag = ymin + (y / hauteur) * (ymax - ymin)
            c = Complexe('z', reel, imag)
            iter_count = mandelbrot(c, max_iter)
            if iter_count == max_iter:
                mandelbrot_image[y, x] = 0  # Points coloriés en noir
    return mandelbrot_image

mandelbrot_image = ensembleMandelbrot(-2.0, 1.0, -1.5, 1.5, 800, 800, 100)

plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_image, cmap='gray', extent=(-2.0, 1.0, -1.5, 1.5))
plt.grid(True, linestyle='--', linewidth=0.5)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.xlabel('Axe des Réels')
plt.ylabel('Axe des Imaginaires')
plt.title("Ensemble de Mandelbrot")
plt.show()



