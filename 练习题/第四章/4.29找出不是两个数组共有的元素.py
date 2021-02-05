a=list(map(int,input().split()))
b=list(map(int,input().split()))
result=[]
for i in a[1:]:
    if i not in b and i not in result:
        result.append(i)
for i in b[1:]:
    if i not in a and i not in result:
        result.append(i)
#*result即直接输出数组内容
print(*result)