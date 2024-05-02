import sys
sys.setrecursionlimit(100001)

from collections import defaultdict

def solution(n, lighthouse):
    graph = defaultdict(set)
    for a, b in lighthouse:
        graph[a].add(b)
        graph[b].add(a)
    lightup = [False] * (n + 1)
    
    
    def check(root, children):
        if not children:
            return False
        if any([(not check(c, graph[c] - {root})) for c in children]):
            lightup[root] = True
            return True


    check(1, graph[1])
    
    return sum(lightup)