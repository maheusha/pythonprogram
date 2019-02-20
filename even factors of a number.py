N=int(raw_input())
d=[]
for x in range(2,N+1):
    if(N%x== 0):
        if(x%2==0):
            d.append(x)
c=" ".join(map(str,d))
print(c)
