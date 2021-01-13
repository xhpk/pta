#方法一
# a=input().split()
# sum=0
# # 计算a中有多少个
# count=0
# # 遍历a
# for i in a:
#     sum+=int(i)
#     count+=1
# avg=sum/count
# for i in a:
#     if int(i)>avg:
#         print(i,end=" ")

#方法二
a=list(map(lambda x:int(x),input().split()))
avg=sum(a)/len(a)
for i in a:
    if int(i) > avg:
        print(i, end=" ")
