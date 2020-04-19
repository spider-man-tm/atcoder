n, a, b, c, d=map(int,input().split())
s = input()
# a->c, b->d
# a<b
if c>d:
  if '...' in s[b-2:d+1]:
    if '##' in s[a:c]:
      print('No')
      exit()
  else:
    print('No')
    exit()
 
else:
  if '##' in s[a:c]:
    print('No')
    exit()
  if '##' in s[b:d]:
    print('No')
    exit()
    
print('Yes')