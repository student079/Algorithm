import sys

eight = sys.stdin.readline().rstrip('\n')

print(bin(int(eight, 8))[2:])
