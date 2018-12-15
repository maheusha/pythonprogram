N,K=map(int,input().split())
c=0
x=K-1
while(c==0 and x>1):
    if(K%x==0 and N%x==0):
        c+=1
    x-=1
print(x+1)
