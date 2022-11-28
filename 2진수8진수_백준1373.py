import sys

two = sys.stdin.readline().rstrip('\n')

print(oct(int(two, 2))[2:])
