#方法一
n=int(input())
sum=0
index=1
for i in range(0,n):
    sum += 1 / index
    index += 2
print("sum = {:.6f}".format(sum))

