#方法一
x=float(input())
if x==0:
    print("f(0.0) = 0.0")
else:
    print("f({:.1f}) = {:.1f}".format(x,1/x))
# #方法二
# x=float(input())
# result=0
# if x !=0:
#     result=1/x
# print("f({:.1f}) = {:.1f}".format(x,result))