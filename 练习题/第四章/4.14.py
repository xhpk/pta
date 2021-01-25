s=[]
count=0;letters=0;space=0;digit=0;others=0
while True:
    b=list(input())
    count=count+1
    s.extend(b)
    if len(s)+count>10:
        count=count-1
        break
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print("letter = {}, blank = {}, digit = {}, other = {}".format(letters,space+count,digit,others))