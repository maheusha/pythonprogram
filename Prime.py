r1=2
r2=10
for n in range(r1,r2):
   if(n>1):
       for i in range(2,n):
          if(n%i)==0:
             break
          else:
             print(n)
             break
