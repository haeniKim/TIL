#제곱수 판별하기 
#n**0.5가 루트 씌운 값이므로 이 값이 자연수라면 제곱수라는 사실까지 유도하기
def solution(n):
    for i in range(1, int(n**0.5)+1):
        if i**2 == n:
            return 1
    return 2

#반복문을 사용하지 않는 풀이
def solution2(n):
    return 1 if (n**0.5).is_integer() else 2