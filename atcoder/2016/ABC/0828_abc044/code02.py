w = input()

# a ~ z までの辞書を生成(valueの初期値は0)
d = {chr(i): 50 for i in range(97, 97+26)}

for c in w:
    d[c] += 1

ans = 'Yes'
for k, v in d.items():
    if v%2==1:
        ans = 'No'
        break

print(ans)