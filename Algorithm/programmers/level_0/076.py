#머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

#반복문 사용하지 않은 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)