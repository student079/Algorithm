import sys
from collections import defaultdict, deque

aeiou = defaultdict(int)
for i in ['a', 'e', 'i', 'o', 'u']:
    aeiou[i] = 1
aeiou[""] = -1

while True:
    pw = sys.stdin.readline().rstrip()
    
    if pw == "end":
        break
    
    # 초기화
    q = deque()
    q.append("")
    q.append("")
    aeiouFlag = False
    check = False

    for i in pw:
        if not aeiouFlag and aeiou[i] == 1:
            aeiouFlag = True
        
        if aeiou[q[0]] == aeiou[q[1]] and aeiou[q[1]] == aeiou[i]:
            break

        if i != "e" and i != "o" and q[1] == i:
            break
        
        q.append(i)
        q.popleft()
    
    else:
        if aeiouFlag:
            check = True


    if not check:
        print("<{}> is not acceptable.".format(pw))
    else:
        print("<{}> is acceptable.".format(pw))
