import sys
import math
# math에 factorial있으니까 참고
n = math.factorial(int(sys.stdin.readline().rstrip('\n')))
n = str(n)
sum = 0

for i in range(len(n)-1, -1, -1):
    if int(n[i]) == 0:
        sum += 1
    else:
        print(sum)
        break
