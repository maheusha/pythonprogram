M=int(raw_input())
c=[]
h=M//60
c.append(h)
m=M%60
c.append(m)
r=" ".join(map(str,c))
print(r)
