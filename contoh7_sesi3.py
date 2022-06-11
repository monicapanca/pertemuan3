#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:05:42 2022

@author: monica
"""

# Function definition is here
def printinfo( name, nilai1, nilai2, nilai3, nakhir ):
   "This prints a passed info into this function"
   nakhir = (nilai1*0.1) + (nilai2*0.2) + (nilai3*0.4)
   
   print("Name: ", name)
   print("nilai 1 : ", nilai1)
   print("nilai 2 : ", nilai2)
   print("nilai 3 : ", nilai3)
   print("nilai akhir : ", nakhir)
   return;

# Now you can call printinfo function
printinfo( name="monica", nilai1=80, nilai2=80, nilai3=70, nakhir=0)