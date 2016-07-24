#!/usr/bin/python
# Filename os_listfile.py

import os

def list_all_file():
    allfiles = os.listdir()
    for fname in allfiles:
        print('fname ' + os.path.abspath(fname)+ ' ' ,os.path.isdir(fname))
        if os.path.isdir(fname):
            os.chdir(fname)
            list_all_file()
            os.chdir('../')

list_all_file()
