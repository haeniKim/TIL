T = int(input()) #테스트 케이스를 입력 받음

for t in range(T): #테스트 수 만큼 반복
    new_s = "" #문자를 담을 변수 생성
    R, S = input().split() #반복할 횟수와 문자열을 입력받아 공백을 기준으로 분리
    for s in S: #문자열의 각 문자에 대해서
        new_s += int(R)*s #문자에 반복 횟수를 곱해 변수에 더함  
    print(new_s) #새로운 문자열을 출력