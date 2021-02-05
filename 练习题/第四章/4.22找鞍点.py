n = int(input())
matrix = []
row_max=[]
col_min=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
    row_max.append(max(matrix[i]))#获取行最值
for i in range(n):
    for j in range(n):
        col_min.append(min(matrix[j][i]))#获取列最值
for i in range(n):#行列遍历比较
    for j in range(n):
        if row_max[i]==col_min[j] and col_min[j]==matrix[i][j]:
            print(i,j)
            exit(0)
print('NONE')