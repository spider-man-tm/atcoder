n = int(input())
st = {}

maxi = 0

for _ in range(n):
    s = input()

    if s in st:
        st[s] += 1
    else:
        st[s] = 1

    if st[s] > maxi:
        maxi = st[s]

ans = []
for k, v in st.items():
    if v==maxi:
        ans.append(k)

ans = sorted(ans)
for a in ans:
    print(a)