list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num  = int(input("Enter a number: "))
found = False
for x in list_num:
    if list_num[x] == num:
        found = True
        break
if found:
    print(f"Number {num} found")
else:
    print(f"Number {num} not found")

