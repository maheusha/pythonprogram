N=int(input())
c=0
for x in range(0,N+1):
    p=str(x)
    c+=p.count('2')
print(c)
