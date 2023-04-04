import sys

N = int(sys.stdin.readline())
if N == 0:
    print("0")
    exit()
res = ""

while N:
    if N%(-2):
        res = '1' + res
        N = N//-2 + 1
    else:
        res = '0' + res
        N //= -2
        
print(res)