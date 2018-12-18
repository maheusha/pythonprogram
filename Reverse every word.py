C=raw_input().split()
L=[]
for i in C:
    L.append(i[::-1])
R=" ".join(L)
print(R)
