from collections import defaultdict

def solution(arrows):
    answer = 0
    
    # 뭔가 2차원배열 쓰는 건 아닌것 같고
    # 대각선 교차도 포함 -> 2칸 씩 이동 좌표 늘려서 
    # 방문했던 거 또 방문에다가 처음 경로면 방 +
    # 경로랑 정점 저장 (무방향이라 양쪽 다 저장)
    
    visited = defaultdict(list)
    dx = (-1,-1,0,1,1,1,0,-1)
    dy = (0,1,1,1,0,-1,-1,-1)
    x,y = 0,0
    for arrow in arrows:
        for _ in range(2):
            nx = x+dx[arrow]
            ny = y+dy[arrow]
            
            # 이 정점은 방문했었지만 이 경로로 방문했던 적 없음
            if (nx,ny) in visited and (x,y) not in visited[(nx,ny)]:
                answer+=1
                visited[(nx,ny)].append((x,y))
                visited[(x,y)].append((nx,ny))
            elif (nx,ny) not in visited:
                visited[(nx,ny)].append((x,y))
                visited[(x,y)].append((nx,ny))
            
            x = nx
            y = ny
    
    
    return answer