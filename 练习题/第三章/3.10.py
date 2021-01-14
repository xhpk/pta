s=input()
a="AEIOU"
count=0
for i in s:
    if i.isupper() and i not in a:
        count+=1
print(count)
