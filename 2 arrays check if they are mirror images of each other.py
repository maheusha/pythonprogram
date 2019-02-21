N= int(raw_input())
L= [ int(x) for x in input().split()]
R= L[::-1]
c=" ".join(map(str,R))
print(c)
d=R[::-1]
if(L==d):
    print("yes")
else:
    print("no")
