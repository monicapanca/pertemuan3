#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:15:23 2022

@author: monic
"""

# Function definition is here
def printinfo( name, age = 26, gender = "male" ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   print("gender: ", gender)
   return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )