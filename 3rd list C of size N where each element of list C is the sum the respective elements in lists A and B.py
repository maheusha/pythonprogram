N=int(input())
l=input().split()
k=input().split()
p=[]
for x in range(0,N):
    c=int(l[x])+int(k[x])
    p.append(c)
    s=" ".join(map(str,p))
print(s)
