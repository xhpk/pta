m, n = map(int,input().split())
#定义三个集合分别保存能整除3,5,7的数
set3 = set()
set5 = set()
set7 = set()
result= set()
for i in range(m, n + 1):
    if (i % 3 == 0):
        set3.add(i)
    if (i % 5 == 0):
        set5.add(i)
    if (i % 7 == 0):
        set7.add(i)
#合并三个集合
result = set3 & set5 & set7
print(len(result))