# 개선된 선택 정렬

## 함수
import random

def selectionSort(ary) :
    n = len(ary)
    for i in range(0, n-1) :
        minIndex = i
        for k in range(i + 1, n) : # 두번째 값부터 마지막 값까지 비교
            if(ary[minIndex] > ary[k]) : 
                minIndex = k
        ary[i], ary[minIndex] = ary[minIndex], ary[i]       

    return ary        

## 변수
dataAry= [random.randint(10,200) for _ in range(20)]



## 메인
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)