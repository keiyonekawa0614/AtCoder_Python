N = int(input())
A = list(map(int, input().split()))
ans = 0

for x in A:
  if x <= 10:
    pass
  else:
    ans += x - 10

print(ans)
