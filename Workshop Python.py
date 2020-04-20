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


# In[70]:


#Classe définissant un compte bancaire avec 2 attributs : nom et prénom
class CompteBancaire:
    
    #nom = 'Dupont'
    #solde = 1000
    
    def __init__(self, nom="Dupont", solde=1000):
        self.nom = nom
        self.solde = solde
        self.ville = "Paris"
    
    def depot(self, montant) :
        self.solde = self.solde + montant
        
    def retrait(self, montant) :
        self.solde = self.solde - montant
        
    def affiche(self) :
        #print("Le solde du compte de "+self.nom)
        #print("Then u have "+ str(self.solde))
        print("{}{}{}{}".format("Le solde du compte de ", self.nom, " est de ", self.solde))


# In[75]:


cmpt2 = CompteBancaire("Toto", 800)
cmpt2.depot(355)
cmpt2.retrait(200)
cmpt2.affiche()


# In[73]:


cmpt = CompteBancaire()
cmpt.depot(35)
cmpt.affiche()


# In[ ]:




