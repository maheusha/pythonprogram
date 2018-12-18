N,K=map(int,raw_input().split())
l=[]
for x in range(0,N):
    l.append(int(input()))
    l.sort()
print(l[N-K])
