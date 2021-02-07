def isPrime(num):
    num=int(num)
    for i in range(2,num):
        if num%i==0 :
            return False
    if(num!=1):
        return True
def PrimeSum(a,b):
    sum=0
    for i in range(a,b+1):
        if isPrime(i):
            sum+=i
    return sum

m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))