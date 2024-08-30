# Tuple functions in python, count, length, occurances, type conversion.

tup = (1, 2, 3, 4, 5)
print(tup[0])
print(tup[2])


print(len(tup))  

print(tup.count(3)) 

print(tup.index(4))

li = list(tup)
print(li)  

tup2 = tuple(li)
print(tup2)