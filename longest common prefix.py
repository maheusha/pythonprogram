i=int(input())
s=input()
p1=input()
s2=[]
for i in range(0,len(s)):
    if s[i]==p1[i]:
        s2.append(s[i])
s=''.join(s2)        
print(s)
        
