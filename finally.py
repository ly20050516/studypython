#!/usr/bin/python
#filename:finally.py

import time

try:
    f = open('poem.txt','r')
    try:
        while True:
            line = f.readline()
            if(len(line) == 0):
                break
            time.sleep(2)
            print(line)
    except:
        print('read file error')
    finally:
        f.close()
        print('cleanup file')
except FileNotFoundError:
    print('open file error')
