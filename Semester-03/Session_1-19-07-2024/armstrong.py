num = int(input("Enter a number "))
arm = 0
temp = num

while temp > 0:
    digit = temp % 10
    arm += digit ** 3
    temp //= 10
    
if num == arm:
    print(f'{num} is an armstrong number')
else:
    print(f'Not an armstrong number')
    