word = input().upper()
alp = list(set(word))

cnt=[word.count(i) for i in alp]

if cnt.count(max(cnt)) > 1:
  print('?')
else:
  print(alp[cnt.index(max(cnt))])