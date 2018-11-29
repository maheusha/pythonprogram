n=raw_input()
for x in range(2,n):
    if(n%x==0):
        print("no")
        break
else:
    print("yes")
