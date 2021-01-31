err=float(input())
Sum=float(1)
a=i=int(1)
while err<=1/a:
    Sum+=1/a
    a*=(i+1)
    i+=1
print('{:.6f}'.format(Sum+1/a))