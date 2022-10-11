s = input() 

for i in range(ord('a'), ord('z')+1): #a-z를 아스키코드값으로 변환하여 반복문 실행
    if chr(i) in s: #a-z 알파벳이 단어 s에 있는 경우
        print(s.index(chr(i)), end = ' ') #해당 알파벳이 있는 곳의 인덱스 값을 반환하고, 한 칸 공백
    else: #알파벳이 단어 s에 없는 경우
        print(-1, end = ' ') #-1을 출력하고 한 칸 공백