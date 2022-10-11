# 1
word = input()
time = 0
for w in word:
  if 'A' <= w <= 'C':
    time += 3
  elif 'D' <= w <= 'F':
    time += 4
  elif 'G' <= w <= 'I':
    time += 5
  elif 'J' <= w <= 'L':
    time += 6
  elif 'M' <= w <= 'O':
    time += 7
  elif 'P' <= w <= 'S':
    time += 8
  elif 'T' <= w <= 'V':
    time += 9
  elif 'W' <= w <= 'Z':
    time += 10  

print(time)

# 2
al_list = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
time = 0

for w in word:
  for a in al_list:
    if w in a:
      time += 3 + al_list.index(a)