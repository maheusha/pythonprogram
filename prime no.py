p=int(raw_input())
for x in range(2,p):
    if(p%x==0):
        print("no")
        break
else:
    print("yes")
