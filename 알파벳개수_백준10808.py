from sys import stdin

word = stdin.readline().strip("\n")
alpha = [0 for i in range(26)]

for i in word:
    alpha[ord(i)-97] += 1

for i in alpha:
    print(i, end=" ")
