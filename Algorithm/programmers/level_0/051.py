#중복된 문자 제거
def solution(my_string):
    non_dup = []
    for i in my_string:
        if i not in non_dup:
            non_dup.append(i)
    answer = ''.join(non_dup)
    return answer

#다른 풀이(굳이 리스트로 만들어 다시 문자열로 만들지 않고 바로 문자열로)
def solution2(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

#다른 풀이 2 (중복이 허용되지 않는 딕셔너리의 키값 특성을 이용)
def solution3(my_string):
    return ''.join(dict.fromkeys(my_string))