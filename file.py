#!/usr/bin/python
#-*- coding:UTF-8 -*-

import os

def readFile(filePath):

    f=open(filePath,'wb')
    i = 1
    while( i <= 9 ):
        j = 1
        while(j <= i):
            str = b'%d * %d = %d '% (j,i,j * i)
            f.write(str)
            print(str)
            j += 1
        f.write(b'\n')
        print('\n')
        i += 1
    f.close()
    return

readFile('test.txt')
