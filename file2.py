f = open('immoc.txt','w')

for i in range(0,100000):
    f.write('write file %d ' % i)

f.close()

f = open('immoc.txt','r')
str = f.read()

print str
