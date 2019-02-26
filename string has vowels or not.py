p=str(raw_input())
c='aeiouAEIOU'
h=0
for x in range(0,len(p)):
    if(p[x] in c):
        h=h+1
    else:
        h=0
if(h>0):
    print("yes")
else:
    print("no")
    
