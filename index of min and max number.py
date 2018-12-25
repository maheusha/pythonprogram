n=int(input())
l1=input().split()
a=[]
for x in l1:
    a.append(int(x))
    m=a.index(min(a))+1,a.index(max(a))+1
print(m)
