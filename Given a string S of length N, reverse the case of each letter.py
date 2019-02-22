N=str(raw_input())
c=[]
for x in range(0,len(N)):
    if N[x].isupper():
        c.append(N[x].lower())
    else:
        c.append(N[x].upper())
d="".join(map(str,c))
print(d)
        
