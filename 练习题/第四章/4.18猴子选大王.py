n=int(input())
if n == 1:
    print(1)
else:
    #设置猴子数量
    monkey=[i for i in range(1,n+1)]
    #当猴子数>=3直接去掉第三个猴子，并将前两个加到最后
    while len(monkey) >= 3:
        monkey.pop(2)
        monkey.append(monkey.pop(0))
        monkey.append(monkey.pop(0))
    #当最后剩余两个猴子胜利的必是第二个
    print(monkey[1])