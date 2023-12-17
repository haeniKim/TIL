#문제 : 0과 1로만 이루어진 문자열 S. S에 있는 모든 숫자를 전부 같게 만드려고할 때, 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것.

# 입력 조건 : 첫째 줄에 0과 1로만 이루어진 문자열 S. S의 길이는 100만보다 작음
# 출력 조건 : 행동의 최소 횟수

# 입력 예시 : 0001100
# 출력 예시 : 1

def flipNum(S):
    #모든 수를 0으로 바꾸기 위한 횟수
    spl_0 = S.split('0')
    cnt_0 = len(spl_0) - spl_0.count('')

    #모든 수를 1로 바꾸기 위한 횟수
    spl_1 = S.split('1')
    cnt_1 = len(spl_1) - spl_1.count('')

    return min(cnt_0, cnt_1)


print(flipNum('0001100'))
print(flipNum('00101011010'))

#--- 다른 풀이 ---
data = input()
count0 = 0 #전부 0으로 바꾸기
count1 = 0 #전부 1로 바꾸기

#첫번째 원소
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

#두번째 원소부터
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        #다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        #다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1
print(min(count0, count1))