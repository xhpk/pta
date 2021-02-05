n = int(input())
sum = 0
for i in range(1,n+1,2):
    k = 1
    for j in range(1,i+1):
        k *= j
    sum += k
print('n={},s={}'.format(n,sum))