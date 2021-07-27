s = input()
s_rev = s[::-1]
t = []

for str in s_rev:
  if str == "6":
    t.append("9")
  elif str == "9":
    t.append("6")
  else:
    t.append(str)

print("".join(t))
