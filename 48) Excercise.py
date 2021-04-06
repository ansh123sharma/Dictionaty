# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:17:33 2021

@author: Dell India
"""
# How Dictionary works:

dict = {"Abandone":"Cancle", "Postpone":"Delaying", "Swag":"Style", "Procastinate":"Delaying"}
print(dict)

try:
    value = input("Please enter the word: ")
    print("Meaning is:",dict[value])  
except Exception as e:
    print("Sorry! we are not able to find the meaning of: ",e)
    
   