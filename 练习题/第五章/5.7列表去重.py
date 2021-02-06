lst = eval(input())
a = []
for i in lst:
    if i not in a:
        a.append(i)
print(*a)