n=int(input())
for i in range(10**(n-1),10**n):
    j=str(i)
    sum=0
    for x in j:
        sum+=int(x)**n
    if sum==i:
        print(i)