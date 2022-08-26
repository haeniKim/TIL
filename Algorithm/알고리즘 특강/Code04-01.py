#단순 연결 리스트

##함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

##변수


##메인
node1 = Node() #비어있는 노드 생성
node1.data = "다현"

node2 = Node() #비어있는 노드 생성
node2.data = "정연"
node1.link = node2 #노드를 연결

node3 = Node() #비어있는 노드 생성
node3.data = "쯔위"
node2.link = node3 #노드를 연결

node4 = Node() #비어있는 노드 생성
node4.data = "사나"
node3.link = node4 #노드를 연결

node5 = Node() #비어있는 노드 생성
node5.data = "지효"
node4.link = node5 #노드를 연결

#삽입
#newNode = Node()
#newNode.data = '해니'
#newNode.link = node2.link
#node2.link = newNode

#삭제
node2.link = node3.link
del(node3)

#print(node1.data, end=" ")
#print(node1.link.data, end =' ')
#print(node1.link.link.data, end =' ')
#print(node1.link.link.link.data, end =' ')
#print(node1.link.link.link.link.data, end =' ') #node1을 기준으로 

current = node1
print(current.data, end = ' ')
while (current.link != None):
    current = current.link
    print(current.data, end= ' ')