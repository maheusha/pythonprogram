n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
c=1
for x in range(0,n):
    c=c*a[x]
p=abs(c)    
print(p)   
