 # 1st way

def check_armstrong(num):
     n = num
     nod = len(str(num))
     result = 0
     while n>0:
         ld = n%10
         result = result + ld**nod
         n = n//10
     return result == num

num = int(input('Enter any number to check armstrong: '))
print(check_armstrong(num))



# 2nd way

num = int(input('Enter any number to check armstrong: '))
n =  num
nod = len(str(num))
result = 0
while n>0:
    ld = n%10
    result = result + ld**nod
    n = n//10
if result == num:
    print('Armstrong number')
else:
    print('Not a Armstrong number')
