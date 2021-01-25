#方法一
num=int(input())
for i in range(0,num):
    n=int(input())
    #定义一个变量表示是否为素数
    isprime = True
    for x in range(2,n):
        if n%x==0:
            isprime=False
            break
    #如果该数不是素数并且不是1
    if isprime and n!=1:
        print("Yes")
    else:
        print("No")

#方法二
#定义一个函数，判断是否为素数
def isPrime(num):
    num=int(num)
    for i in range(2,num):
        if num%i==0 :
            return False
    if(num!=1):
        return True
n = int(input())
for i in range(1,n+1):
    t=int(input())
    if(isPrime(t)):
        print("Yes")
    else:
        print("No")
        