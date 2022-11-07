item = int(input())
lst = []
for i in range(item):
    n, m = map(int, input().split())
    lst.append([n, m])
rounds = []
lst_len = len(lst)
for i in lst:
    round = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            round += 1

    rounds.append(round)

for i in rounds:
    print(i, end=" ")
