number = int(input("Enter a number: "))
rev = 0
digit = 0

while number != 0:
    digit = number % 10
    rev = rev * 10 + digit
    number //= 10
    
print(f'Here is the reversed number: {rev}') 