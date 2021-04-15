n, s, d = map(int, input().split())

def check():
  x, y = map(int, input().split())
  return x < s and y > d

if any(check() for i in  range(n)):
  print("Yes")
else:
  print("No")
