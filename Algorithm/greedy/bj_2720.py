# 세탁소 사장 동혁
# 문제 : 거스름돈의 액수가 주어지면 쿼터, 다임, 니켈, 페니의 개수를 구하는 프로그램

# 입력 : 테스트 케이스 T, 각 테스트 케이스는 거스름돈 C 단위는 센트, 1달러 = 100센트
# 출력 : 각 테스트케이스에 대해 필요한 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 공백으로 구분하여 출력

#예제 입력:
# 3
# 124
# 25
# 194

#예제 출력:
# 4 2 0 4
# 1 0 0 0
# 7 1 1 4

# 풀이 
T = int(input())

for tmp in range(T):
    C = int(input())
    q, C = divmod(C, 25)
    d, C = divmod(C, 10)
    n, C = divmod(C, 5)
    p = C
    print(f"{q} {d} {n} {p}")

# -- 함수화 --
def charge():
    C = int(input())
    q, C = divmod(C, 25)
    d, C = divmod(C, 10)
    n, C = divmod(C, 5)
    p = C
    return f"{q} {d} {n} {p}"

T = int(input())

for tmp in range(T):
    print(charge())
    

