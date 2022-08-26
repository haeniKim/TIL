# 이진 검색 
## 함수
import random
def binSearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary) - 1
    while (start <= end) :
        mid = (start + end) // 2 
        if fData == ary[mid] :
            pos = mid
            break
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1      
    return pos


## 변수
dataAry= [random.randint(10,20000) for _ in range(1000)]
dataAry.sort()
findData = random.choice(dataAry)


## 메인
print('배열 --> ', dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
    print(f'{findData}는 없음')
else :
    print(f'{findData}는 {position}위치에 있음')