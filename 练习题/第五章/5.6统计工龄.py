a = int(input())
age = list(map(int, input().split()))
dic = {}
for i in age:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
#按键值排序后输出
for j in sorted(dic.keys()):
    print('{}:{}'.format(j, dic[j]))