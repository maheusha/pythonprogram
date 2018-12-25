m=int(input())
N=input().split()
l=[]
p=0
for x in N:
    l.append(int(x))
for x in l:
    if(l.count(x)==1):
        print(x)
