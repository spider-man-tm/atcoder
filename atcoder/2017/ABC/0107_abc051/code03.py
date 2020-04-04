# UU  R     DD  L
#LUUU RR DR DDD LLU

sx, sy, tx, ty = map(int, input().split())
print('U'*abs(ty-sy),
        'R'*abs(tx-sx),
        'D'*abs(ty-sy),
        'L'*abs(tx-sx),
        'L',
        'U'*(abs(ty-sy)+1),
        'R'*(abs(tx-sx)+1),
        'DR',
        'D'*(abs(ty-sy)+1),
        'L'*(abs(tx-sx)+1),
        'U',
        sep='')