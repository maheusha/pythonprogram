n=raw_input()
n<=1000
a=[]
for i in range(1,n+1):
    a.append(int(input()))
for i in range(0,n):
    print(a[i],i)
