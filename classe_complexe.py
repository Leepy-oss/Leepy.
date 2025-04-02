# Créé par lepeeben, le 04/11/2024 en Python 3.7

from math import *
import numpy as np
from sympy import Rational


class Complexe:
    def __init__(self,nom,a=0,b=0):
        self.nom = nom
        self.reel=a
        self.imaginaire=b

    def get_partieReelle(self):
        return self.reel

    def get_partieImaginaire(self):
        return self.imaginaire

    def get_complexe(self):
        return self.reel+self.imaginaire*1j

    def get_nom(self):
        return self.nom

    def set_partieReelle(self,a):
        self.reel=a

    def set_partieImaginaire(self,b):
        self.imaginaire=b

    def conjuguate(self):
        self.imaginaire=-self.imaginaire
        return self.reel+self.imaginaire*1j

    def carre(self):
        self.reel=self.reel**2 - self.imaginaire**2
        self.imaginaire=2*self.reel*self.imaginaire
        return self.reel+self.imaginaire*1j

    def module(self):
        mod=sqrt((self.reel**2)+(self.imaginaire**2))
        return np.round(mod)

    def argument(self):
        mod = self.module()
        theta1 = np.arctan2(self.imaginaire/mod , self.reel/mod)
        if theta1 <0:
            theta2 = theta1 + 2*np.pi
        else:
            theta2 = theta1
        rad=Rational(theta2 / np.pi).limit_denominator()
        arg = '('+ str(rad)+')'+'π'
        return arg

    def formeTrigonometrique(self):
        mod = self.module()
        arg = self.argument()
        Tf= str(mod) + '(cos('+arg+')'+'+'+'jsin('+arg+')'+')'
        return Tf

    def formeExponentielle(self):
        mod = self.module()
        arg = self.argument()
        Ef= str(mod) + 'exp('+arg+'j)'
        return Ef


    def __str__(self):
        if self.reel==0 and self.imaginaire==0:
            ch="Votre nombre complexee "+str(self.get_nom())+" est nul. Sa partie réelle et sa partie Imaginaire sont nulles, de même que pour son module et son argument n'est donc pas défini."
        elif self.reel==0:
            ch='Votre nombre complexee '+str(self.get_nom())+ ' est un Imaginaire pur: '+ str(self.get_complexe()) + ', sa partie Imaginaire vaut donc: '+ str(self.imaginaire) + '.' + '\n'
            ch+= 'Son module est défini par: '+ str(self.module())+'.'+' , son argument par: ' + self.argument() + '. Sa forme trigonométrique est donc: ' + self.formeTrigonometrique() + '\n'
            ch+='et sa forme exponentielle est donnée par: ' + self.formeExponentielle()
        elif self.imaginaire==0:
            ch='Votre nombre complexee '+str(self.get_nom())+' est un Réel pur: '+str(self.reel)+'. Son module est défini par: '+str(self.module())+', son argument par: ' + self.argument() + '.' + '\n'
            ch+= 'Sa forme trigonométrique est donc: ' + self.formeTrigonometrique() + ' et sa forme exponentielle est donnée par: ' + self.formeExponentielle()
        else:
            ch='Votre nombre complexee '+str(self.get_nom())+' est: '+str(self.reel+self.imaginaire*1j)+', sa partie réelle est: '
            ch+=str(self.reel)+' et sa partie imaginaire est: '+str(self.imaginaire)+'.' + '\n' + 'Son module est défini par: '+str(self.module())+', son argument par: ' + self.argument() + '\n'
            ch+='Sa forme trigonométrique est donc: ' + self.formeTrigonometrique() + ' et sa forme exponentielle est donnée par: ' + self.formeExponentielle()
        return ch

z1 = Complexe("z1",-2,-2*sqrt(3))





