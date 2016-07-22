#!/usr/bin/pyton
# Filename:cpickle.py
# load & dump

#import cPickle as p,python 3 cann't use
import pickle as p

shoplistfile = 'shoplist.data'

shoplist = ['apple','mango','carrot']

f = open(shoplistfile,'wb')
p.dump(shoplist,f)
f.close()

del shoplist

f = open(shoplistfile,'rb')
storedlist = p.load(f)
print(storedlist)
f.close()
