num = int(input())
cnt = num
for i in range(num):
  word = input()
  for w in range(len(word)-1):
    if word[w] == word[w+1]:
      pass
    elif word[w] in word[w+1:]:
      cnt -= 1
      break

print(cnt)