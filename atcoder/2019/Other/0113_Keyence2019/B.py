s = input()
for start in range(len(s)):
    for end in range(start, len(s)+1):
        st = s[:start]+s[end:]
        if st=='keyence':
            print('YES')
            exit()

print('NO')