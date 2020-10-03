a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

pi = ['x'] * 10

for i in p:
    pi[i] = '.'
for i in q:
    pi[i] = 'o'

print(f'{pi[7]} {pi[8]} {pi[9]} {pi[0]}')
print(f' {pi[4]} {pi[5]} {pi[6]}')
print(f'  {pi[2]} {pi[3]}')
print(f'   {pi[1]}')
