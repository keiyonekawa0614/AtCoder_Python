n = input()
sum = 0

for x in n:
  sum += int(x)

if sum % 9 == 0:
  print("Yes")
else:
  print("No")
