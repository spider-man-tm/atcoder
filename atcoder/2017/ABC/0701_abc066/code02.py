string = input()

for i in range(len(string)):
    s = string[:-(i+1)]

    if len(s)%2 == 1:
        continue
    else:
        half = int(len(s)/2)
        s1 = s[:half]
        s2 = s[half:]

        if s1 == s2:
            print(half*2)
            break