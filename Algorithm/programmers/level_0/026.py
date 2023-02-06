#각도기
def solution(angle):
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
    return answer

#다른 풀이
#def solution(angle):
#   answer =  (angle // 90) * 2 + (angle % 90) * 1
#   return answer