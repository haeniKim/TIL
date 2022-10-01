import sys
n, x = map(int,sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(nums)):
    if nums[i] < x:
        print(nums[i], end = " ")