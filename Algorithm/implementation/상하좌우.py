#문제 : 
# N X N 정사각형 공간 -> 이동시 벗어날 수 없음.
# 문자 : L, R, U, D





# 입력 조건 : 첫째 줄에 공간의 크기를 나타내는 N이 주어진다 (1 <= N <= 100)
#           둘쩨 줄에 여행가 A가 이동할 계획서 내용이 주어진다 (1 <= 이동 횟수 <= 100)

# 출력 조건 : 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다. 

# 입력 예시 :
# 5 
# R R R U D D
# 출력 예시 :
# 3 4

N = int(input())
moves = input().split()
x, y = 1, 1

for m in moves:
    if m == 'U' and x != 1:
        x -= 1
    elif m == 'D' and x != N:
        x += 1
    elif m == 'L' and y != 1:
        y -= 1
    elif m == 'R' and y != N:
        y += 1
    else:
        continue

print(x, y)