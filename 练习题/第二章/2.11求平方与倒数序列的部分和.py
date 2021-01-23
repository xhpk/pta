# a,b=input().split()
# a=int(a)
# b=int(b)
# sum=0
# for i in range(a,b+1):
#     sum=sum+i**2+1/i
# print("sum = {:.6f}".format(sum))

#方法二
from functools import reduce
a,b=map(lambda x:int(x),(input().split()))
#这里注意reduce是将上一个结果与下一个参数相运算，再最开始时会从前两个数开始计算
#比如这里是a-1,a
sum=reduce(lambda x,y:x+(y**2+1/y),range(a-1,b+1))
print("sum = {:.6f}".format(sum-(a-1)))