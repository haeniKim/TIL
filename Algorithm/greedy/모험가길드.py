# 01 모험가 길드
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있음
# 최대 몇 개의 모험가 그룹을 만들 수 있는지
# N 명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최대값

n  = int(input())
fears = list(map(int, input().split()))
fears.sort()

# 총 그룹 수
result = 0

# 그룹 내 인원 수 
cnt = 0

for f in fears:
    #그룹에 인원 추가
    cnt += 1
    if (cnt >= f):
        result += 1
        cnt = 0

print(result)


