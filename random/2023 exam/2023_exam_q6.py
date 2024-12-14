def log(b, n):
    count = 0

    while n >= b:
        n /= b
        count += 1
    return count

print(log(2, 1))