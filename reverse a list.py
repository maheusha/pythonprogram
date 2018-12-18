N= int(input())
L= [ int(x) for x in input().split()]
R= L[::-1]
p= len(R)
for i in range(0,p-1) :
    print(R[i],end='->')
print(R[p-1])
