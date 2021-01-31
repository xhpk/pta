#定义一个函数判断是否为质数
def isprime(n):
    if n<=1:
        return False
    #int(n**0.5+1)防止超时
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True

n=int(input())
for x in range(2,n):
    if isprime(x) and isprime(n-x):
        print('{} = {} + {}'.format(n,x,n-x))
        break