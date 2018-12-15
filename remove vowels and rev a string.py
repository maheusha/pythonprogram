n=int(raw_input())
a=raw_input()
for x in "aeiouAEIOU":
    a=a.replace(x,"")
    s=str(a)[::-1]
print(s)
