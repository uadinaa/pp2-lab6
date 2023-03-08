f = open('A.txt','r')
s = open('C.txt','w')

for i in f:
    s.write(i)