num=int(input())
sum=1
b=1
for i in range(1,num+1):
    b=b*i
    c=+ 1 / b
    sum=sum+c
print("{:.8f}".format(sum))