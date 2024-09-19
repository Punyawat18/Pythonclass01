a = [1, 2, 3, 4]
print(id(a))
print(id(a[3]))
print(a)
a.append(5)
print(id(a))
print(id(a[3]))
print(id(a[4]))

print(a)
b = 1
print(id(b))
b = 2
print(id(b))
x = [1, 4, 2, 3, 5, 4]
x = list(filter(lambda o: o != 4, x))
print(x)