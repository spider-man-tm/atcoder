week = {
    'SUN': 7,
    'MON': 6,
    'TUE': 5,
    'WED': 4,
    'THU': 3,
    'FRI': 2,
    'SAT': 1,
}

s = input()
print(week[s])


"""別解
S = input()
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
 
print(7 - days.index(S))
"""