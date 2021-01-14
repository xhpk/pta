lst=input().split()[1:]
count={}
max=-1
index=-1
#计算每个数的频次
for  i in lst:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
#找出最大
for key,value in count.items():
    if value>max:
        max=value
        index=key
print(index,max)
