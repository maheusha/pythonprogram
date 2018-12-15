N,K=map(int,raw_input().split())
c=0
x=K-1
while(c==0 and x>1):
    if(N%x==0 and K%x==0):
        c+=1
    x-=1
print(x+1)
