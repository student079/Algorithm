import sys

N = int(sys.stdin.readline().rstrip('\n'))

arr = [[0, 0, 0], [1, 1, 1]]

for i in range(2, N+1):
    temp = [sum(arr[i-1]) % 9901, (arr[i-1][0] + arr[i-1][2]) %
            9901, (arr[i-1][0]+arr[i-1][1]) % 9901]
    arr.append(temp)

print(sum(arr[N]) % 9901)
