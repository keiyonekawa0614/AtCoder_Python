N = int(input())

def solve():
  money = 0
  day = 1
  while True:
    money += day
    if money >= N:
      return day
    day += 1

print(solve())
