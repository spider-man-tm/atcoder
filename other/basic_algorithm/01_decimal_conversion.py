def decimal_conversion(n, k):
    ans = ''
    while n > 0:
        ans = str(n%k) + ans
        n //= k

    return int(ans)

print(decimal_conversion(100, 2))  # 1100100
print(bin(100)) # 0b1100100