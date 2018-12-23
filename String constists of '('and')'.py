S=str(raw_input())
c=0
for x in range(0,len(S)):
    if(S[x]=='('):
        c=c+1
    if(S[x]==')'):
        c=c-1
if(c==0):
  print("yes")
else:
    print("no")
        
