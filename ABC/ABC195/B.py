import math

A, B, W = map(int, input().split())
upper = int(math.floor(W * 1000 / A))
lower = int(math.ceil(W * 1000 / B))
if lower > upper:
  print("UNSATISFIABLE")
else:
  print(lower, upper)
