# #方法一
# #导入math包
# from math import sqrt
# a,b,c=input().split()
# a=int(a)
# b=int(b)
# c=int(c)
# if a+b<=c or a+c<=b or b+c<=a:
#     print("These sides do not correspond to a valid triangle")
# else:
#     s=(a+b+c)/2
#     #sqrt表示开方
#     area=sqrt(s*(s-a)*(s-b)*(s-c))
#     c=a+b+c
#     print("area = {:.2f}; perimeter = {:.2f}".format(s,c))

#方法二
a,b,c=map(lambda x:int(x),input().split())
if a+b<=c or a+c<=b or b+c<=a:
    print("These sides do not correspond to a valid triangle")
else:
    s=(a+b+c)/2
    #sqrt表示开方
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    c=a+b+c
    print("area = {:.2f}; perimeter = {:.2f}".format(s,c))