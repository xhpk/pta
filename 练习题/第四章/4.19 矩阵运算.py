n=int(input())
a=[]
sum=0
for i in range(n):
    s=input()
    a.append([int(n) for n in s.split()])
for j in range(n):
    for k in range(n):
        if j!=n-1 and k!=n-1 and j+k!=n-1:
            sum+=a[j][k]
print(sum)