#方法一
a,b=input().split()
a,b=int(a),int(b)
sum=0
t=0
for i in range(1,b+1):
    t=t*10+a
    sum=sum+t
print("s = ",sum)

#方法二
a,n=input().split()
sum=0
for i in range(1,int(n)+1):
    sum+=int(a*i)
print("s =",sum)