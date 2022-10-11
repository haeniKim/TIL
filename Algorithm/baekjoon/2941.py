# 1
cro_list = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']
word = input()
cnt = len(word)

for c in cro_list:
  cnt -= word.count(c)

print(cnt)

# 2
cro_list = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']
word = input()

for c in cro_list:
  word = word.replace(c,'*')

print(len(word))