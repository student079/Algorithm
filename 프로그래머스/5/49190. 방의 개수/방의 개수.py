from collections import defaultdict

def solution(arrows):
    answer = 0
    
    # 정수아닌 부분이 겹칠 수도 있으니 *2
    # 좌표 넣다가 좌표 겹치고 들어온 좌표도 똑같으면 안해도됨
    # 들어온 좌표가 다르면 +1
    
    dx = (-1,-1,0,1,1,1,0,-1)
    dy = (0, 1, 1, 1, 0, -1, -1,-1)
    
    # 딕셔너리로 저장하자 들어온 좌표를
    x,y = 0, 0
    p_visited = defaultdict(list)
    p_visited[(x,y)].append((x,y))
    for arrow in arrows:
        for _ in range(2):
            
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            
            if (nx, ny) in p_visited.keys():
                if (x,y) not in p_visited[(nx,ny)]:
                    answer += 1
                    p_visited[(nx, ny)].append((x, y))
                    p_visited[(x,y)].append((nx,ny))
            else:
                p_visited[(nx, ny)].append((x, y))
                p_visited[(x,y)].append((nx,ny))
                
            x,y = nx, ny
    
    return answer