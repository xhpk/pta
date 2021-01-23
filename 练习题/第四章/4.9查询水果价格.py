print("[1] apple")
print("[2] pear")
print("[3] orange")
print("[4] grape")
print("[0] exit")

price = [0.00, 3.00, 2.50, 4.10, 10.20]
lst = list(map(int, input().split()))
count = 0
for i in lst:
    if i == 0:
        break
    elif 1 <= i <= 4:
        print('price = {:.2f}'.format(price[i]))
    else:
        print('price = 0.00')
    count += 1
    if count == 5:
        break