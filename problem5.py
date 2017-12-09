squares=[]
for x in range(10):
    squares.append(x**2)

print(squares)

print(list(map(lambda x:x**2,range(10))))
print(list(x**2 for x in range(10)))