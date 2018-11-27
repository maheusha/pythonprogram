n=(raw_input())
c=0
p=(raw_input())
a=[]
for x in range(0,n):
    a.append(int(input()))
    if(x<=p+1):
        s=c+x
print(s)
