def swap(a: int, b: int):
    b -= a
    a += b
    
    b = a - b
    
    return a, b

a, b = 27, 84
print(a, b)
a, b = swap(a, b)
print(a, b)
a, b = swap(a, b)
print(a, b)

print('=' * 100)

a, b = 72, 14
print(a, b)
a, b = swap(a, b)
print(a, b)
a, b = swap(a, b)
print(a, b)
