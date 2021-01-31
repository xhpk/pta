m,n=map(int,input().split())
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
print('{:d} {:d}'.format(gcd(n,m),n*m//gcd(n,m)))