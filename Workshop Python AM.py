#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn



# In[2]:


class MyClass :
    def meth(test):
        print('wsh world')
        
t = MyClass()
t.meth()


# In[7]:


class OtherClass :
    def test_meth(self):
        return self
        
txt = OtherClass()
txt.test_meth()


# In[12]:


class CompteBancaire :
    def __init__(nom = 'Dupont', solde = 1000) :
        print("Le solde du compte bancaire de "+nom+"est de "+solde)
        
        
cmpt = CompteBancaire()


# In[13]:


class CompteBancaire :
    def __init__(nom = 'Dupont', solde = 1000) :
        print("Le solde du compte bancaire de "+nom+"est de "+solde)
        
        
cmpt = CompteBancaire()


# In[84]:


#Classe définissant un compte bancaire avec 2 attributs : nom et prénom
class CompteBancaire:
    
    def __init__(self, nom="Dupont", solde=1000): #Default value si on passe rien au init()
        self.nom = nom
        self.solde = solde
        #self.ville = "Paris"
    
    def depot(self, montant) :
        self.solde = self.solde + montant
        
    def retrait(self, montant) :
        self.solde = self.solde - montant
        
    def affiche(self) :
        #print("Le solde du compte de "+self.nom)
        #print("Then u have "+ str(self.solde))
        print("{}{}{}{}".format("Le solde du compte de ", self.nom, " est de ", self.solde))


# In[85]:


cmpt2 = CompteBancaire("Toto", 667)
cmpt2.depot(355)
cmpt2.retrait(200)
cmpt2.affiche()


# In[86]:


cmpt = CompteBancaire()
cmpt.depot(35)
cmpt.affiche()


# In[ ]:





# In[ ]:





# In[ ]:





# In[99]:


#La surchage d'opérateur

class Point:
    
    def __init__(self, x =0,y =0,z =0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def ToString(self):
        if self.z != 0:
            print( "{}{}{}{}{}{}{}".format("P(",str(self.x), ", ",str(self.y),", ",str(self.z),")") )
        else:
            print("{}{}{}{}{}".format("P(",str(self.x), ", ",str(self.y),")") )


# In[101]:



P1 = Point(5,7)
P1.ToString()


# In[102]:


P2 = Point(3,5,7)
P2.ToString()


# In[105]:


class DateNaissance:
    def __init__(self, jour, mois, annee):
        self.jour = int(jour)
        self.mois = int(mois)
        self.annee = int(annee)
        
    def ToString(self):
        print("Date de naissance :"+str(self.jour)+" / "+str(self.mois)+" / "+str(self.annee))


# In[106]:


Dtn = DateNaissance(10, 7, 1920)
Dtn.ToString()


# In[107]:


class Person :
    def __init(self, nom, prenom, DateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.DateNaissance = DateNaissance
        
    def afficher(self):
        print("Nom :"+ str(self.nom))
        print("Prenom :"+ str(self.prenom))
        print("Naissance :"+ self.DateNaissance.ToString())


# In[108]:


class Employe(Person):
    def __init__(self,salaire):
        Person.__init__(self, nom, prenom,DateNaissance)
        self.salaire = salaire
        
        def afficher(self):
            Person.afficher(self)
            print("Salaire :"+ str(self.salaire))


# In[ ]:


class Chef(Employe):
    def __init__(self, service):
        Employe.__init__

