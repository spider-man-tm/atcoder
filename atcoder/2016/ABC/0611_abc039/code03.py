s = input()[:12]

onkai = {
    'WBWBWWBWBWBW': 'Do',
    'WBWWBWBWBWWB': 'Re',
    'WWBWBWBWWBWB': 'Mi',
    'WBWBWBWWBWBW': 'Fa',
    'WBWBWWBWBWWB': 'So',
    'WBWWBWBWWBWB': 'La',
    'WWBWBWWBWBWB': 'Si',
}

print(onkai[s])