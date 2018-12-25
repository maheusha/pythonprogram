N,K=map(int,raw_input().split())
P=list(str(N))
while(K>0):
    K=K-1
    del(P[K])
R=(''.join(P))
print(R)
