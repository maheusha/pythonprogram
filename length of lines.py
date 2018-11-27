a=input()
d=1
for i in range(0,len(a)):
    if(a[i]=="."):
        d=d+1
    else:
        d=d
print(d)
