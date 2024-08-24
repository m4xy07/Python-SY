var_a = int(input("Enter the first number: "))
var_b = int(input("Enter the second number: "))
var_c = int(input("Enter the third number: "))

if var_a > var_b and var_a > var_c:
   print(f'{var_a} is the greatest number')
elif var_b > var_a and var_b > var_c:
    print(f'{var_b} is the greatest number')
else:
    print(f'{var_c} is the greatest number')
    