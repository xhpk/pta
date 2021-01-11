a=input().split()
#先将输入转成Int类型
for i in range(0,3):
    a[i]=int(a[i])
# 利用sort()自动排序
a.sort()
print("{}->{}->{}".format(a[0],a[1],a[2]))