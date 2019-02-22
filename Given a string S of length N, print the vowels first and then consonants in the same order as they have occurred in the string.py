N=(raw_input())
q=['a','e','i','o','u','A','E','I','O','U']
d=[]
j=[]
for x in range(0,len(N)):
    if N[x] in q:
        d.append(N[x])
    else:
        j.append(N[x])
m=d+j
c=''.join(map(str,m))
print(c)
    

