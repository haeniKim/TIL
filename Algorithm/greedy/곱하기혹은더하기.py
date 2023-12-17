# 문제 : 각 자라기 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+' 연산자를 
# 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성.
# 단 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어짐

# 입력 조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S
# 출력 조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수 출력

# 입력 예시 : 02984
# 출력 예시 : 576

def maxResult(S):
    result = int(S[0])
    for num in S[1:]:
        num = int(num)
        if result <= 1 or num <= 1:
            result += num
        else:
            result *= num
    return result

    # 0일 때는 +, 1은 +, 


print(maxResult('02984'))

print(maxResult('567'))