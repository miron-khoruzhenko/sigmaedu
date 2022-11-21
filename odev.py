# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:39:23 2022

@author: mrtyz
"""

sıralama = ""
for x in range (0, 10):
    for y in range (0, 10):
        if y> x:
            sıralama += (str(x)+ str(y) + ", ")
print( sıralama [:-2])            