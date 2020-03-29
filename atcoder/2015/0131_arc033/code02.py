Na, Nb = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

iou = len(A & B)/len(A | B)
print(iou)