lower=(raw_input())
upper=(raw_input())
for num in range(lower,upper+1):
    order=len(str(num))
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum +=digit**order
        temp//=10
    if num==sum:
        print(num)
