a=raw_input().split()
c=[]
for x in a:
    c.append(x[::-1])
k=" ".join(c)
print(k)
