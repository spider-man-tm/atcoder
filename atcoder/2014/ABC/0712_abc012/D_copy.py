from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import floyd_warshall
import numpy as np

INF = float('inf')

N, M = map(int, input().split())
A, B, C = [], [], []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    A.append(a)
    B.append(b)
    C.append(c)

D = coo_matrix((C, (A, B)), (N, N)).tocsr()
d = floyd_warshall(D, directed=False)

"""
print(D)
[out]
  (0, 1)        10
  (1, 2)        10

print(d)
[out]
[[ 0. 10. 20.]
 [10.  0. 10.]
 [20. 10.  0.]]
"""

print(int(np.min(np.max(d, axis=0))))