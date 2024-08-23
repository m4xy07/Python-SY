l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("Enter a number: "))
found = False
low = 0
high = len(l1) - 1
while low <= high:
    mid = (low + high) // 2
    if l1[mid] == num:
        found = True
        break
    elif l1[mid] < num:
        low = mid + 1
    else:
        high = mid - 1
if found:
    print(f"Number {num} found")
else:
    print(f"Number {num} not found")
    