import sys


# 단어들 셋으로 받고
# 알파벳에서 K개 순서 상관없이 뽑는 경우
# dfs, 백트래킹으로 구현
# 알파벳 26개니까 리스트 활용
# a,n,t,i,c는 포함되어야함 -> K가 5보다 작으면 걍 0
# 26이면 걍 N
# 참개수 출력

# 글자로 단어 만들 수 있는지 확인
def check(word):
    for i in word:
        if not alpha[ord(i) - ord('a')]:
            return False
    return True
ans = 0

def comb(idx , count):
    global ans
    if count == K - 5:
        s = 0
        for i in words:
            if check(i):
                s+=1
        ans = max(ans,s)

        if ans == N:
            print(ans)
            exit()

        return
    
    for k in range(idx,26):
        if not alpha[k]:
            alpha[k] = True
            comb(k + 1,count+1)
            alpha[k] = False


N, K = map(int,sys.stdin.readline().split())

words = []
for _ in range(N):
    words.append(set(sys.stdin.readline().rstrip('\n')))\
    
if K < 5:
    print('0')
    exit()
elif K >= 26:
    print(N)
    exit()

alpha = [False] * 26

for i in {'a','n','c','i','t'}:
    alpha[ord(i) - ord('a')] = True

comb(0,0)
print(ans)

