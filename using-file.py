#!/usr/bin/python

poem = '''\
Programming is fun when the work is done.if you wanna make your work also fun:use Python!'''

f = open('poem.txt','w')
f.write(poem)
f.close()

f = open('poem.txt','r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()
