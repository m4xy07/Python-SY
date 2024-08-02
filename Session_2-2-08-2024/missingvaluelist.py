# Program to find a missing element in a given list

l1 = list(map(int, input("Enter values seperated by a space ").split(" ")))

for x in range(len(l1)):
    if l1[x+1] != l1[x]+1:
        print(l1[x]+1)
        
# n * (n+1) / 2 - sum (l1)