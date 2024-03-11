# 최대 K개의 집중국
# N개의 센서 집중국 수신가능 길이의 합이 최소

import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = sorted(list(map(int,sys.stdin.readline().rstrip().split())))

# 센서들간의 거리 차
diff = sorted([sensors[i+1] - sensors[i]for i in range(N-1)])

# 거리차이가 큰거 부터K-1개 빼주고 합
print(sum(diff[:N-K]))
