# N, M 5000

# eof
import sys

def check(num):
    nums = [0] * 10
    for c in str(num):
        c = int(c)
        if nums[c] > 0:
            return False
        else:
            nums[c] += 1
    return True

while True:
    try:
        N, M = map(int,sys.stdin.readline().rstrip().split())
        answer = 0
        for i in range(N, M+1):
            if check(i):
                answer+=1
        print(answer)

    except EOFError:
        break
    except ValueError:
        break

