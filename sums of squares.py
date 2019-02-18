N=int(raw_input())
sum=0
while(N>0):
    n=int(N%10)
    sum=(n*n)+sum
    N=int(N/10)
print(sum)
