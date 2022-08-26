#완전한 선택 정렬

## 함수
import random
def findMinIndex(ary) :
    minIndex = 0
    for i in range(1, len(ary)) :
        if (ary[minIndex] > ary[i]) :
            minIndex = i
    return minIndex

## 변수
before = [random.randint(10,200) for _ in range(20)]
after = []


## 메인
print('정렬 전 -->', before)
for i in range(len(before)) :
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])

print('정렬 후 -->', after)