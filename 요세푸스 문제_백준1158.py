import sys

N, K = map(int,sys.stdin.readline().split())

people = [i for i in range(1, N+1)]
res = []

idx = 0
for i in range(N):
    lengP = len(people)
    #K-1씩 더하면서 people[idx]pop해주기
    idx += (K-1)
    #people의 길이를 넘으면 idx를 길이로 나눈 나머지 값으로 만들기
    if idx >= lengP:
        idx %= lengP
    res.append(str(people[idx]))
    people.pop(idx)

#출력값 처리 sep: 기본설정인" "를 피하기 위함
print("<",", ".join(res),">",sep="")