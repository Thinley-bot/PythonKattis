num = 16461
temp=num
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if reversed_num==temp:
    print("it is palindrome")
else:
    print("not palindrome")

