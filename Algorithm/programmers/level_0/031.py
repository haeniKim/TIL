#진료 순서 정하기
def solution(emergency):
    dic = {k:v+1 for v, k in enumerate(sorted(emergency, reverse = True))}
    answer = [dic[i] for i in emergency]
    return answer