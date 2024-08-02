# # Method 1
# l1 = input("Enter ")
# print(l1)
# l3 = []
# for x in l1:
#     if x != " ":
#         x = int(x)
#         l3.append(x)

# print(sum(l3))

# Method 2 using map
l1 = list(map(int, input("Enter values seperated by a space ").split(" ")))
print(l1)
print(sum(l1))

