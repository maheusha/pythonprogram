l=str(raw_input())
a=[]
for m in l:
    if(m not in a):
        a.append(m)
c="".join(map(str,a))
print(c)
