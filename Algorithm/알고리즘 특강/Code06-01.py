#스택

## 함수


## 변수
#stack = [None, None, None, None, None]
SIZE = 5
stack = [None for _ in range(SIZE)] #스택 초기화
top = -1 #초기화


## 메인
## Push : 삽입
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print('바닥 :', stack)

## Pop : 추출
data = stack[top]
stack[top] = None
top -= 1
print("팝 --> ", data)


print("바닥 : ", stack)