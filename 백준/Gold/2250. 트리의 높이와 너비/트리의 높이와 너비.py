import sys

class Node:
	def __init__(self, number, leftNode, rightNode):
		self.parent = -1
		self.number = number
		self.leftNode = leftNode
		self.rightNode = rightNode

def inorder(node, level):
	global levelDepth, x
	levelDepth = max(levelDepth, level)
	
	if node.leftNode != -1: # 왼쪽 노드 방문
		inorder(tree[node.leftNode], level+1)
	levelMin[level] = min(levelMin[level], x)
	levelMax[level] = max(levelMax[level], x)
	x += 1
	if node.rightNode != -1: # 오른쪽 노드 방문
		inorder(tree[node.rightNode], level+1)
		
n = int(sys.stdin.readline())
tree = {}
levelMin = [n]
levelMax = [0]
root = -1
x = 1
levelDepth = 1

for i in range(1,n+1):
	tree[i] = Node(i, -1, -1) # 트리 초기화, 모두 비어있다고 가정
	levelMin.append(n)
	levelMax.append(0)


for _ in range(n):
	number, leftNode, rightNode = map(int, sys.stdin.readline().split())
	tree[number].leftNode = leftNode
	tree[number].rightNode = rightNode
	
	# 자식 노드 있으면 부모가 있다고 체크(부모 노드 값을 parent에 넣어줌)
	if leftNode != -1:
		tree[leftNode].parent = number
	if rightNode != -1:
		tree[rightNode].parent = number
		
for i in range(1, n+1):
	if tree[i].parent == -1: # 부모가 없는 노드 -> 루트
		root = i
		
inorder(tree[root], 1)


result_level = 1
result_width = levelMax[1] - levelMin[1] + 1

for i in range(2, levelDepth+1):
	width = levelMax[i] - levelMin[i] + 1 # 너비
	if result_width < width: # 가장 넓은 너비일 경우
		result_level = i
		result_width = width
		
print(result_level, result_width)