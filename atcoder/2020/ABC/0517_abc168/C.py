import math

A, B, H, M = map(int, input().split())

ka_a = ((H/12) * 360) + (30*(M/60))
ka_b = M/60 * 360

kakudo = max(ka_a, ka_b) - min(ka_a, ka_b)
kakudo = min(kakudo, (360-kakudo))
cos = math.cos(math.radians(kakudo))

if kakudo==180:
    print(A+B)
    exit()

ans = A**2 + B**2 - 2*A*B*cos

print(math.sqrt(ans))