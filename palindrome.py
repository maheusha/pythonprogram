p=int(raw_input())
p<=1000
t=p
reverse=0
while(p>0):
    digi=p%10
    reverse=reverse*10+digi
    p=p//10
if(t==reverse):
    print("yes")
else:
    print("no")
