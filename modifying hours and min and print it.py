H,M=map(int,raw_input().split())
H1,M1=map(int,raw_input().split())
c=[]
h=abs(H-H1)
c.append(h)
m=abs(M-M1)
c.append(m)
r=" ".join(map(str,c))
print(r)
