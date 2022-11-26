# 유클리드 호제법 사용
import sys
# 재귀 깊이 조절
sys.setrecursionlimit(10**6)

def gcd(a, b):
    r = a % b
    if r != 0 : 
        return gcd(b,r)
    else:
        return b

a,b = map(int, sys.stdin.readline().rstrip('\n').split())

minn = gcd(a,b)
maxn = int(a*b/minn)


print(minn)
print(maxn)