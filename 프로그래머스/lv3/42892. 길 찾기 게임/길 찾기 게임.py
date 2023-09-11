from sys import setrecursionlimit

def solution(nodeinfo):
    
    # 파이썬은 기본적으로 1000까지만 재귀가 들어가도록
    # 이 문제는 최대 10000까지 재귀가 들어갈 수 있으므로 재설정
    setrecursionlimit(10000)
    
    # 트리구조 만들기
    class Node:
        def __init__(self, info):
            self.left = None
            self.right = None
            self.pos = info[:2]
            self.idx = info[2]
    
    # 전위 순회, 후위 순회
    
    # 노드 번호 넣어주고, y값 큰 순, x 값 작은 순서로 sort
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key = lambda x : (x[1], -x[0]), reverse = True)
    
    # 트리
    def add_node(parent, node):
        if parent.pos[0] > node[0]:
            if parent.left:
                add_node(parent.left, node)
            else:
                parent.left = Node(node)
        else:
            if parent.right:
                add_node(parent.right, node)
            else:
                parent.right = Node(node)
    
    # 트리구성
    tree = Node(nodeinfo[0])
    for node in nodeinfo[1:]:
        add_node(tree, node)
    
    # 전위 순회
    preanswer = []
    def preorder(preanswer, tree):
        preanswer.append(tree.idx)
        if tree.left:
            preorder(preanswer, tree.left)
        if tree.right:
            preorder(preanswer, tree.right)
    preorder(preanswer, tree)
    
    # 후위순회
    postanswer = []
    def postorder(postanswer, tree):
        if tree.left:
            postorder(postanswer, tree.left)
        if tree.right:
            postorder(postanswer, tree.right)
        postanswer.append(tree.idx)
    postorder(postanswer, tree)

    return [preanswer, postanswer]