#문제 : N개의 동전을 이용해 만들 수 없는 양의 정수 금액 중 최솟값을 구하기




# 입력 조건 : 첫째 줄에는 동전의 개수를 나타내는 양의 정수 N (1이상 1000이하)
#            둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며 공백으로 구분

# 출력 조건 : 첫째 줄에 주어진 동전으로 만들 수 없는 양의 정수 금액 중 최솟값을 출력

# 입력 예시 :
# 5
# 3 2 1 1 9
# 출력 예시 :
# 8

N = int(input())

coin  = list(map(int, input().split()))

#nums =  n_list
# [1,5,2,5,6]

#from itertools import combinations

#for i in range(2, N+1):
#    for c in combinations(n_list, i):
#        nums.append(sum(c))

#nums = set(nums)
#print(nums)

##ordered_num = [i for i in range(1, sum(n_list)+1)]
#print(ordered_num)

#for n in ordered_num:
#    if n not in nums:
#        print(n)
#       break


