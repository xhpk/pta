m,n=input().split()
#sum表示最后的和,count表示质数个数
sum=0
count=0
for i in range (int(m),int(n)+1):
    #定义一个变量表示是否为素数
    isprime = True
    for x in range(2,i):
        if i%x==0:
            isprime=False
            break
    #如果该数不是素数并且不是1
    if isprime and i!=1:
        count+=1
        sum+=i
print(count,sum)

