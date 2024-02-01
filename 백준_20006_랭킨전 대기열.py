import sys

# 매칭가능한 방 X -> 새로운 방 생성 -> 입장
# 처음입장한 플레이어 레벨 기준으로 +-10까지 입장 가능
# 매칭 가능한 방 O -> 입장 -> 정원 다 찰때까지 대기
# 매칭 가능한 방 여러개 -> 먼저 생성된 방
# 정원 다 차면 게임 시작

rooms = []

p, m = map(int, sys.stdin.readline().split())

def ready(level, nickname):
    
    for room in rooms:
        l, n = room[0]

        if (l - 10 <= level <= l + 10) and len(room) < m:
            room.append((level, nickname))
            level = 0
            break
    
    if level != 0:
        rooms.append([(level, nickname)])



for _ in range(p):
    l, n = sys.stdin.readline().split()

    ready(int(l), n.rstrip())

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    
    room.sort(key = lambda x : x[1])
    for player in room:
        print(*player)
