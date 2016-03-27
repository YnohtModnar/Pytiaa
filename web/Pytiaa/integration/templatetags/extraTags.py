import os
from django import template

register = template.Library()

@register.filter()
def getDirect(path):
    path = '/home/randomtony/Documents/Programmes/git/Pytiaa/web/Pytiaa/static/img/'+path
    direc=[]
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            direc.append(i)
    direc.sort()

    return [(i,direc[i]) for i in range(len(direc)) ]

@register.filter()
def getImages(direc):
    img=[]

    path ='/home/randomtony/Documents/Programmes/git/Pytiaa/web/Pytiaa/static/img/'+direc
    for i in os.listdir(path):
        if not os.path.isdir(os.path.join(path, i)) and i.split('.')[-1]=="png":
            img.append(int(i.split('.')[0]))
    img.sort()
    return [(i,str(img[i])+".png") for i in range(len(img)) ]
