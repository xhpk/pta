num=int(input())
max_str=""
for i in range(num):
    s=input()
    if len(s)>len(max_str):
        max_str=s
print("The longest is:",max_str)