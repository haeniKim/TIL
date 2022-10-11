n = int(input())
for i in range(n):
  cnt = 0
  sum = 0
  ox = input()
  for j in ox:
    if j == "O":
      cnt += 1
      sum += cnt
    elif j == "X":
      cnt = 0
  print(sum)