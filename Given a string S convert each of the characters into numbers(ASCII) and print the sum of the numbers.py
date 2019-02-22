N=raw_input()
l=[]
j=0
for x in range(0,len(N)):
    c=ord(N[x])
    l.append(c)
for i in range(0,len(l)):
    j=j+l[i]
print(j)
    
