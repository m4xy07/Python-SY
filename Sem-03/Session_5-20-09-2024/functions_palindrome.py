def is_palindrome(value):
    value_str = str(value)
    reversed_str = value_str[::-1]
    return value_str == reversed_str


print(is_palindrome("radar"))
print(is_palindrome("hello"))  
print(is_palindrome(12321))   
print(is_palindrome(12345)) 