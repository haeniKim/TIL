def d(n):
  result = n
  for i in range(len(str(n))):
    result += int(str(n)[i])
  return result 
  
  d_list = [d(n) for n in range(1,10001)]
  
  for i in range(1,10001):
    if i not in d_list:
        print(i)