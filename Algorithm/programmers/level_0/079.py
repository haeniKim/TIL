#최댓값 만들기 (2) 
#중첩 for문 이용, 두 원소 곱들을 모두 구한 리스트에서 최대값
def solution(numbers):
    mul = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            mul.append(numbers[i] * numbers[j])
    return max(mul)

#다른 풀이
#단순하게 음수의 경우 정렬 후 가장 작은 값 두개의 곱으로 최대값을 판정할 수 있음
def solution2(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 