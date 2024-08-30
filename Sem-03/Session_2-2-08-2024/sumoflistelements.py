
l1 = [x for x in range(1, int(input("Enter value of n ")))]
print(l1)

#Method 1 to iterate through elements
sum = 0

for x in l1:
    sum += x
    
print(f"Total of all elements is {sum}")
