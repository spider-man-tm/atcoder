n = int(input())
s = input()
east = [0] * n
west = [0] * n
before_east, before_west = 0, 0

for i in range(n):
    if s[i] == 'E':
        east[i] = before_east+1
        west[i] = before_west
        before_east = east[i]
        before_west = west[i]
    else:
        east[i] = before_east
        west[i] = before_west+1
        before_east = east[i]
        before_west = west[i]

total_east = east[-1]
total_west = west[-1]

mini = float('inf')
for i in range(n):
    if i==0:
        left_east, left_west = 0, 0
        if s[0]=='E':
            right_east = total_east-1
            right_west = total_west
        else:
            right_east = total_east
            right_west = total_west-1
    else:
        left_east = east[i-1]
        left_west = west[i-1]
        right_east = total_east-east[i]
        right_west = total_west-west[i]

    tmp = left_west+right_east

    if tmp<mini:
        mini = tmp

print(mini)