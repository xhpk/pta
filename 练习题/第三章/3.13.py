x = input()
for ch in x:
    if ch.isupper():
        #ord()计算字符ASCII码，chr根据ASCII码得出字符
        ch = chr(ord('Z') - ord(ch) + ord('A'))
    print(ch, end = "")