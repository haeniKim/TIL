import sys
cnt = 0

n = int(sys.stdin.readline().rstrip())
m = n
while True:
  n1 = (m // 10) + (m % 10)
  m = (m % 10) * 10 + (n1 % 10)
  cnt += 1
  if n == m :
    print(cnt)
    break