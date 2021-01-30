def rec(s):
    """dfs"""
    if len(s) == N:
        print(s)
    else:
        res = set(s)
        res.add(chr(ord(max(res)) + 1))
        res = sorted(list(res))
        for i in res:
            rec(s + i)
 
 
N = int(input())
 
rec("a")