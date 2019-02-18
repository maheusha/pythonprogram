N=int(raw_input())
d=[]
for x in range(1,N+1):
    if(N%x==0):
        d.append(int(x))
        c=" ".join(map(str,d))
print(c)
