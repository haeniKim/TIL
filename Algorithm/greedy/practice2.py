# 큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
## 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해 더해질 수 없다.

#배열 크기 N, 숫자 더해지는 횟수 M, 그리고 K

# 입력 조건:
# 첫째 줄에 N M K (K는 항상 M보다 작거나 같음)
# 둘째 줄에 N개의 자연수, 공백으로 구분

# 출력 조건:
# 동빈이의 큰 수 법칙에 따른 답

# 입력 예시:
# 5 8 3
# 2 4 5 4 6

# 출력 예시:
# 46

## 나의 풀이
N, M, K = map(int, input().split())
N_list = list(map(int, input().split()))

# 1. list 내림차순 정렬
N_list.sort(reverse=True)

# 2. 횟수 M번 중, 연속이지 않게 다음 큰 수가 나오는 횟수를 구해 계산한다.
cnt = M // (K+1)
num = (N_list[0] * (M-cnt)) + (N_list[1] * cnt)

print(num)


## 단순하게 푸는 답안
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result  = 0

while True: # m번 동안 가장 큰 수가 k번 더해지고, 그 다음 큰 수가 한 번씩 더해지는 것을 반복 
    for i in range(k): #가장 큰 수 k번 더하기
        if m == 0: # m이 0이면 탈출
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

## 다른 답안 
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * K
count += m % (k + 1)

result  = 0
result += (count) * first
result += (m - count) * second

print(result)