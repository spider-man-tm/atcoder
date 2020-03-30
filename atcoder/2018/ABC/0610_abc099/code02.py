a, b = map(int, input().split())
diff = b-a
high = (1+diff)*(diff/2)
print(int(high-b))