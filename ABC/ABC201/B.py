N = int(input())
L = []

for _ in range(N):
  s, t = input().split()
  t = int(t)
  L.append((t, s))

L.sort(reverse = True)
print(L[1][1])

