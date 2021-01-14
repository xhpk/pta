n=int(input())
num=list(map(int,input().split()))
index=0
for i in range(0,n):
    if num[i]>num[index]:
        index=i
print(num[index],index)