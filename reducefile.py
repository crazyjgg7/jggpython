#encoding='utf-8'
import os

from functools import reduce 


def readfile(filename):
    with open(filename,'r',encoding='utf-8')as files:
        content = reduce(lambda x,y:x+y,files.readlines())
        return content
file=readfile('data.txt')
print(file)


