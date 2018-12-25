N=int(raw_input())
a=[]
m=1
for i in range(0,N):
    a.append(int(input()))
for x in range(0,N):
    m=m*a[x]   
print(m)   
