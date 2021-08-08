N = int(input())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = float('INF')

for i in range(N):
    for j in range(N):
        if i == j:
            score = A[i] + B[i]
        else:
            score = max(A[i], B[j])
        ans = min(ans, score)

print(ans)
