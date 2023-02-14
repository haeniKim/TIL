#한 번만 등장한 문자
def solution(s):
    single = [i for i in s if s.count(i) == 1]
    answer = ''.join(sorted(single))
    return answer