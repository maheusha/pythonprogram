n=int(input())
l1=input().split()
a=[]
for x in l1:
    a.append(int(x))
print(a.index(min(a))+1,a.index(max(a))+1)
    
   
