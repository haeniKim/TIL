#완전버전 큐 _ 개선
#문제 : 큐 크기가 많을 때는 데이터 당길 때 시간이 오래 소요 -> 해결 : 원형 큐

## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :
        return False
    elif (rear == SIZE-1 and front == -1) :
        return True
    else :
        for i in range(front+1,SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if isQueueFull() :
        print("큐 꽉 찼음")
        return
    rear += 1
    queue[rear] = data


def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐 비었음")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐 비었음")
        return None
    return queue[front+1]

## 변수
SIZE = 5
queue = [ None for _ in range(SIZE)]
front = rear = -1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('[출구]<--', queue, '<--[입구]')

retData = deQueue()
print('식사손님 :', retData)
retData = peek()
print(f'{retData}님 준비하세요')
retData = deQueue()
print('식사손님 :', retData)
#retData = deQueue()
#print('식사손님 :', retData)
#retData = deQueue()
#print('식사손님 :', retData)
print('[출구]<--', queue, '<--[입구]')

enQueue('제니')
print('[출구]<--', queue, '<--[입구]')