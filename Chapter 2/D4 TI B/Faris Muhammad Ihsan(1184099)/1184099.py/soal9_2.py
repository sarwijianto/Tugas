# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:23:19 2019

@author: Faris Fatin 32
"""


i=0
npm = input("NPM: ")
while i<1:
    if len(npm)<7:
        print("npm kurang dari 7")
        npm = input("NPM: ")
    elif len(npm)>7:
        print("npm lebih dari 7")
        npm = input("NPM: ")
    else:
        i=1
        
a=npm[0]
b=npm[1]
c=npm[2]
d=npm[3]
e=npm[4]
f=npm[5]
g=npm[6]


for x in a,b,c,d,e,f,g:
    
    if int(x)%2==0:
        if int(x)==0:
            x=""
        print(x,end ="")