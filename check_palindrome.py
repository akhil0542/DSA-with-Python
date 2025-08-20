# 1st way without function

num = int(input('Enter any number to check palindrome: '))
n = num
result = 0
while n>0:
    last_digit = n%10
    result = result*10 + last_digit
    n = n//10
if result == num:
    print('Palindrome')
else:
    print('Not a Palindrome')



# 2nd way using function

def check_palindrome(num):
    n = num
    result = 0
    while n>0:
        last_digit = n%10
        result = result*10 + last_digit
        n = n//10
    return result == num
number = int(input('Enter any number to check palindrome: '))
print(check_palindrome(number))
