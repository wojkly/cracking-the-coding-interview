def multiply(a: int, b: int) -> int:
    if b == 1:
        return a
    return a + multiply(a, b - 1)

print(multiply(10, 19))