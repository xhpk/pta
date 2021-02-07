def CountDigit(number,digit ):
    number,digit = str(number),str(digit)
    return number.count(digit)

number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)