A, B, C, D = map(int, input().split())
def solve():
  Const = 10 ** 7 + 5
  for x in range(Const):
    cyan = A + B * x
    red = C * x
    if cyan <= D * red:
      return x
  return -1

print(solve())
